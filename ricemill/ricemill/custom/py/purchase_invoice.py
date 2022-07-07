from datetime import datetime
import frappe


@frappe.whitelist()
def get_last_purchase_invoice_details(item_code,last_purchase):
    rate = frappe.get_all("Purchase Invoice Item", filters={
                          "item_code": item_code}, fields=["item_code", "rate", "parent", "qty"], order_by="`creation` desc", limit=last_purchase)
    suppliers = []
    if(len(rate)):
        for i in rate:
            suppliers = frappe.get_all("Purchase Invoice", filters={
                "name": i.parent}, fields=["supplier", "posting_date"])
            i.update(suppliers[0])
            del i['parent']
        return rate
    return 0



