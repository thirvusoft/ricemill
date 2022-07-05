from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def bin_customize():
    bin_field_customize()
    property_setter_bin()

def bin_field_customize():
    custom_fields = {
        "Bin": [
            dict(
                    fieldname="stock_level",
                    label="Total Stock Level",
                    fieldtype="Float",
                    insert_after="stock_value",
                    hidden=1
                ),
        ],
    }
    create_custom_fields(custom_fields)


def property_setter_bin():
    pass