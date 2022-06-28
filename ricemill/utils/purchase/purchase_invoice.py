from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def purchase_invoice_customize_field():
    purchase_invoice_custom_fields = {
        "Purchase Invoice": [
            dict(fieldname='commission_field',
                label='Commission',
                fieldtype='Section Break',
                insert_after='project',
                 collapsible=1
               ),
               dict(fieldname='ts_purchase_partner', 
                label='Purchase Partner',
                fieldtype='Link', 
                options='Purchase Partner',
                insert_after='commission_field',
                ),
                dict(fieldname='ts_account', 
                label='Is Accountable',
                fieldtype='Check',  
                insert_after='ts_purchase_partner'),

                dict(fieldname='commission_account', 
                label='Commission Account',
                fieldtype='Link', 
                options='Account',
                insert_after='ts_account',
                depends_on='eval:doc.ts_account'

               ),
                dict( 
                fieldtype='Column Break', 
                fieldname='column_break20',
                insert_after='ts_purchase_commission_account'),
                
               

                dict(fieldname='ts_commission_rate', 
                label='Commission Rate (%)',
                fieldtype='Data', 
                insert_after='column_break20',
                fetch_from='ts_purchase_partner.commission_rate'),

                dict(fieldname='total_commission', 
                label='Total Commission Rate ',
                fieldtype='Float', 
                insert_after='ts_commission_rate')  
                ]
                }

    create_custom_fields(purchase_invoice_custom_fields)



