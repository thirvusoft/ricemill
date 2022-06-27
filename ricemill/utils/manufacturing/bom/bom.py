from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def bom_customize_field():
    bom_custom_fields = {
        "BOM Operation": [
            dict(fieldname='section_break_warehouse',
                label='Warehouse',
                fieldtype='Section Break',
                insert_after='time_in_mins',
               ),
            dict(fieldname="source_warehouse",
                label="Source Warehouse",
                fieldtype="Link",
                options="Warehouse",
                insert_after="section_break_warehouse",
                reqd=1
                ),
            dict(fieldname="target_warehouse",
                label="Target Warehouse",
                fieldtype="Link",
                options="Warehouse",
                insert_after="source_warehouse",
                reqd=1
                ),
            dict(fieldname="stock_entry_type",
                label="Stock Entry Type",
                fieldtype="Link",
                options="Stock Entry Type",
                insert_after="target_warehouse",
                reqd=1
                ),
            
            ],
        "BOM":[
            dict(fieldname='section_break_bom',
                label='Work Order Status',
                fieldtype='Section Break',
                insert_after='amended_from',
               ),
            dict(fieldname="linked_work_order",
                label="Linked Work Order",
                fieldtype="Table",
                options="TS Work Order Status",
                insert_after="section_break_bom",
                reqd=1
                ),
        ]
            }

    create_custom_fields(bom_custom_fields)

