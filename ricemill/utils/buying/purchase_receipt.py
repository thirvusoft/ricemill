from cProfile import label
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def purchase_receipt_customize_field():
    purchase_receipt_customize_field = {
        "Purchase Receipt": [
            dict(fieldname="section_break1",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='items'
                 ),
            dict(fieldname="last_purchase_item",
                 label='Last Purchase Item',
                 fieldtype='Link',
                 options="Item",
                 read_only=1,
                 insert_after='section_break1'
                 ),
            dict(fieldname="column_break11",
                 fieldtype='Column Break',
                 insert_after='last_purchase_item'
                 ),
            dict(fieldname="last_purchase_supplier",
                 label='Last Purchase Supplier',
                 fieldtype='Link',
                 options="Supplier",
                 read_only=1,
                 insert_after='column_break11'
                 ),
            dict(fieldname="column_break12",
                 fieldtype='Column Break',
                 insert_after='last_purchase_supplier'
                 ),
            dict(fieldname="last_purchase_rate",
                 label='Last Purchase Rate',
                 fieldtype='Currency',
                 read_only=1,
                 insert_after='column_break12'
                 ),
            dict(fieldname="vechile_no",
                 label='Vechile No',
                 fieldtype='Data',
                 insert_after='supplier_delivery_note'
                 )
        ]
    }

    create_custom_fields(purchase_receipt_customize_field)
