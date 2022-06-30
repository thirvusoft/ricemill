import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_stock_entry_custom_field():
    se_fields = {
        "Stock Entry":[
            dict(fieldname="ts_work_order",
            label="TS Work Order",
            fieldtype="Data",
            insert_after="work_order",
            read_only = 1
            )
        ]
    }
    create_custom_fields(se_fields)
    frappe.db.commit()