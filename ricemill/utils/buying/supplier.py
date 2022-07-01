from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def supplier_custom_fields():
    supplier_custom_fields = {
        "Supplier": [
            dict(fieldname='territory',
                 label='Territory',
                 fieldtype='Link',
                 options="Territory",
                 insert_after='supplier_name'
                 )
        ]
    }

    create_custom_fields(supplier_custom_fields)
