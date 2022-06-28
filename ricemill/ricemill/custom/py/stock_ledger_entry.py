import frappe
from erpnext.stock.stock_ledger import get_previous_sle
from frappe.utils import nowdate, nowtime

def validate_warehouse(doc, action):
        frappe.db.commit()
        warehouse=frappe.get_doc("Warehouse", doc.warehouse)
        if warehouse.capacity==1:
                get_valuation_rate(doc.warehouse)
                warehouse_qty=get_valuation_rate(doc.warehouse)+doc.actual_qty
                if warehouse.block==1 and warehouse_qty > warehouse.warehouse_capacity:
                    frappe.throw(f"Capacity of the Warehouse is {warehouse.warehouse_capacity}. You try to reach the limit" )
                elif(warehouse.block==0):
                    frappe.throw("In this warehouse transacations are not allowed")
                
def get_valuation_rate(warehouse):
    qty=0
    for item_code in frappe.get_all('Item',pluck='name'):
        args = {
            "item_code": item_code,
            "warehouse": warehouse,
            "posting_date": nowdate(),
            "posting_time": nowtime(),
        }
        last_entry = get_previous_sle(args)
        qty+=last_entry.qty_after_transaction if last_entry else 0.0
    return qty
