import frappe
from erpnext.stock.stock_ledger import get_previous_sle
from frappe.utils import nowdate, nowtime


def validate_warehouse(doc, action):
    if doc.doctype == "Purchase Invoice":
        if doc.update_stock == 0:
            return

    m = {}
    for i in doc.items:
        if i.warehouse not in m.keys():
            m[i.warehouse] = i.qty
        else:
            m[i.warehouse] = m[i.warehouse] + i.qty
    for j in list(m.keys()):

        bin = sum(frappe.db.get_all(
            "Bin", {"warehouse": j}, pluck="actual_qty"))
        m[j] = m[j]+bin

    for k in list(m.keys()):
        warehouse, block = frappe.db.get_value(
            "Warehouse", k, ["warehouse_capacity", "block"])
        if block == 1 and m[j] > warehouse:
            frappe.throw(
                f"Capacity of the Warehouse is {warehouse} . You try to reach the limit. Exisiting Capacity {sum(frappe.db.get_all('Bin', {'warehouse': k}, pluck='actual_qty'))}. Inward quantity is {m[k]-sum(frappe.db.get_all('Bin', {'warehouse': k}, pluck='actual_qty'))}")

    # warehouse = frappe.get_doc("Warehouse", i.warehouse)
    # if warehouse.capacity == 1:
    #     get_valuation_rate(warehouse)
    #     warehouse_qty = get_valuation_rate(warehouse)+i.qty
    #     if warehouse.block == 1 and warehouse_qty > warehouse.warehouse_capacity:
    #         frappe.throw(
    #             f"Capacity of the Warehouse is {warehouse.warehouse_capacity}. You try to reach the limit")
    #     elif(warehouse.block == 0):
    #         frappe.throw("In this warehouse transacations are not allowed")


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
