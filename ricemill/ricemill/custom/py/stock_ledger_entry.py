import frappe
from erpnext.stock.stock_ledger import get_previous_sle
from frappe.utils import nowdate, nowtime
from erpnext.stock.doctype.batch.batch import get_batch_qty


def validate_warehouse(doc, action):
    if doc.doctype == "Purchase Invoice":
        if doc.update_stock == 0:
            return
    if(doc.doctype not in ['Purchase Invoice', 'Purchase Receipt']):return
    dict = {}
    for items in doc.items:
        if items.warehouse not in dict.keys():
            dict[items.warehouse] = items.stock_qty
        else:
            dict[items.warehouse] = dict[items.warehouse] + items.stock_qty
    for keys in list(dict.keys()):

        bin = sum(frappe.db.get_all(
            "Bin", {"warehouse": keys}, pluck="actual_qty"))
        dict[keys] = dict[keys]+bin

    for value in list(dict.keys()):
        warehouse, block = frappe.db.get_value(
            "Warehouse", value, ["warehouse_capacity", "block"])
        if block == 1 and dict[value] > warehouse:
            frappe.throw(
                f"Capacity of the Warehouse is {warehouse} . You try to reach the limit. Exisiting Capacity {sum(frappe.db.get_all('Bin', {'warehouse': value}, pluck='actual_qty'))}. Inward quantity is {dict[value]-sum(frappe.db.get_all('Bin', {'warehouse': value}, pluck='actual_qty'))}")


def get_valuation_rate(warehouse):
    qty = 0
    for item_code in frappe.get_all('Item', pluck='name'):
        args = {
            "item_code": item_code,
            "warehouse": warehouse,
            "posting_date": nowdate(),
            "posting_time": nowtime(),
        }
        last_entry = get_previous_sle(args)
        qty += last_entry.qty_after_transaction if last_entry else 0.0
    return qty


def create_stock_entry(self, action):
    ref_doctype = self.voucher_type
    ref_docname = self.voucher_no
    if ref_doctype == "Purchase Receipt" or ref_doctype == "Purchase Invoice":
        cur_doc = frappe.get_doc(ref_doctype, ref_docname)
        for i in cur_doc.items:
            if i.warehouse == self.warehouse and i.item_code == self.item_code and i.batch_configuration == "Merge with Existing Batch":
                create_stock(self,1,i.select_batch,i.item_code)
            elif i.warehouse == self.warehouse and i.item_code == self.item_code and i.batch_configuration == "Merge with Incoming Batch":
                create_stock(self,2,i.select_batch,i.item_code)
            if i.warehouse == self.warehouse and i.item_conversion_type == "Merge with Existing Item":
                create_stock(self,1,i.select_item_conversion_batch,i.ts_select_item_conversion)
            elif i.warehouse == self.warehouse and i.item_conversion_type == "Merge with Incoming Item":
                create_stock(self,2,i.select_item_conversion_batch,i.ts_select_item_conversion )

def create_stock(self,act_as,batch,item_code=None):
    batch_qty=frappe.get_all("Stock Ledger Entry",filters={"item_code": self.item_code, "warehouse":self.warehouse,"qty_after_transaction":[">",0],"batch_no":batch}, fields=["qty_after_transaction"],order_by="posting_date desc",
		limit=1)
    batch_qty = get_batch_qty(batch_no=batch, warehouse=self.warehouse, item_code=self.item_code)
    if(batch_qty):
        tot_qty = (batch_qty or 0)+self.actual_qty
        stock_entry = frappe.new_doc("Stock Entry")
        stock_entry.stock_entry_type = "Repack"
        stock_entry.purpose = "Repack"
        stock_entry.ts_ref_doctype = self.voucher_type
        stock_entry.ts_ref_document = self.voucher_no
        if act_as == 1:
            stock_entry.append(
                "items",
                dict(
                    s_warehouse=self.warehouse,
                    qty=self.actual_qty,
                    batch_no=self.batch_no,
                    item_code=self.item_code
                ),
            )
            stock_entry.append(
                "items",
                dict(
                    s_warehouse =self.warehouse,
                    qty =batch_qty,
                    batch_no =batch,
                    item_code = item_code
                ),
            )
            stock_entry.append(
                "items",
                dict(
                    t_warehouse =self.warehouse,
                    qty =tot_qty,
                    batch_no =batch,
                    item_code = item_code
                ),
            )
        elif act_as == 2:
            stock_entry.append(
                "items",
                dict(
                    s_warehouse =self.warehouse,
                    qty =batch_qty,
                    batch_no =batch,
                    item_code = item_code
                ),
            )
            stock_entry.append(
                "items",
                dict(
                    s_warehouse=self.warehouse,
                    qty=self.actual_qty,
                    batch_no=self.batch_no,
                    item_code=self.item_code
                ),
            )
            stock_entry.append(
                "items",
                dict(
                    t_warehouse=self.warehouse,
                    qty=tot_qty,
                    batch_no=self.batch_no,
                    item_code=self.item_code
                ),
            )
        stock_entry.insert()
        stock_entry.save()
