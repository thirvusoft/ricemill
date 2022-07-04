import frappe


@frappe.whitelist()
def get_last_purchase_invoice_details(item_code):
    rate = frappe.get_all("Purchase Invoice Item", filters={
                          "item_code": item_code}, fields=["rate", "parent"], order_by="`creation` desc", limit=1)
    suppliers = []
    if(len(rate)):
        suppliers = frappe.get_all("Purchase Invoice", filters={
            "name": rate[0]["parent"]}, fields=["supplier", "name"])
        return rate[0]["parent"], suppliers[0]["supplier"], rate[0]["rate"]



