from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def work_order_customize_field():
        work_order_custom_field = {
            "Work Order": [
                dict(fieldname='ts_work_order_status', 
                label='Linked Work Order',
                fieldtype='Table',
                options='TS Work Order Status',
                insert_after='company',
                reqd=1),
                dict(fieldname='ts_parent_work_order',
                    label='Parent WorkOrder',
                    fieldtype='Data',
                    insert_after='ts_work_order_status')
            ],
            "Work Order Operation":[
              dict(fieldname="ts_source_warehouse",
              label='Source Warehouse',
              fieldtype='Link',
              options="Warehouse",
              insert_after='workstation'
              ),
              dict(fieldname="ts_target_warehouse",
              label='Target Warehouse',
              fieldtype='Link',
              options="Warehouse",
              insert_after='ts_source_warehouse'
              ),
              dict(fieldname="ts_stock_entry_type",
              label='Stock Entry Type',
              fieldtype='Link',
              options="Stock Entry Type",
              insert_after='ts_target_warehouse'
              )                 
              
            ]
            }
        create_custom_fields(work_order_custom_field)

