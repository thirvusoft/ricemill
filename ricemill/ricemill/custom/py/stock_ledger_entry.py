import frappe
from erpnext.stock.stock_ledger import get_previous_sle
from frappe.utils import nowdate, nowtime


def validate_warehouse(doc, action):
    if doc.doctype == "Purchase Invoice":
        if doc.update_stock == 0:
            return

    dict = {}
    for items in doc.items:
        if items.warehouse not in dict.keys():
            dict[items.warehouse] = items.qty
        else:
            dict[items.warehouse] = dict[items.warehouse] + items.qty
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
