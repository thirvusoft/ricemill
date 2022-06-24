from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def customize_field():
    custom_fields = {
        "Sales Invoice": [
            dict(fieldname='ts_account', label='Is Accountable',
                fieldtype='Check', insert_after='sales_partner'),
            dict(fieldname='commission_account', label='Commission Account',
                fieldtype='Link', options='Account',insert_after='ts_account',depends_on='eval:doc.ts_account')
                ]
                }

    create_custom_fields(custom_fields)

