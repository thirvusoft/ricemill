from dataclasses import fields
from warnings import filters
import frappe


@frappe.whitelist()
def get_last_purchase_details(item_code):
    rate = frappe.get_all("Purchase Order Item", filters={
                          "item_code": item_code}, fields=["rate", "parent"], order_by="`creation` desc", limit=1)
    suppliers = []
    if(len(rate)):
        suppliers = frappe.get_all("Purchase Order", filters={
            "name": rate[0]["parent"]}, fields=["supplier", "name"])
        return rate[0]["parent"], suppliers[0]["supplier"], rate[0]["rate"]

