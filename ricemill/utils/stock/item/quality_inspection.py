from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def quality_inspection_customize_field():
    make_property_setter("Quality Inspection", "reference_type", "options","Purchase Receipt\nPurchase Invoice\nDelivery Note\nSales Invoice\nStock Entry\nJob Card\nWork Order",""),
    make_property_setter("Quality Inspection", "inspection_type", "options","\nIncoming\nOutgoing\nIn Process",""),

def quality_inspection_fields():
     custom_fields = {
        "Quality Inspection": [
            dict(fieldname="accepted_rejected_qty",
            label="Accepted/Rejected Qty",
            fieldtype="Data",
            insert_after="batch_no",
            reqd=1
            )
        ]
    }
     create_custom_fields(custom_fields)

