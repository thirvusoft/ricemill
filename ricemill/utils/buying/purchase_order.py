from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from requests import options


def purchase_order_customize_field():
    purchase_order_customize_field = {
        "Purchase Order": [
            dict(fieldname="section_break1",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='items'
                 ),
            dict(fieldname="last_purchase",
                 label='Select Last Purchase Limit',
                 fieldtype='Select',
                 insert_after='section_break1',
                 options="5\n4\n3\n2\n1",
                 default="3"
                 ),
            dict(fieldname="ts_last_purchase_item",
                 label='Last Purchase Item',
                 fieldtype='Table',
                 options="Last Purchase Item List Details",
                 read_only=1,
                 insert_after='last_purchase'
                 ),
            dict(fieldname="section_break2",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='ts_last_purchase_item'
                 ),
            dict(fieldname="user_name",
                 label='User Name',
                 fieldtype='Data',
                 insert_after='inter_company_order_reference'
                 ),
        ]
    }

    create_custom_fields(purchase_order_customize_field)
