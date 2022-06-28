from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def customize_work_order():
  work_order_customize_field()
  work_card_property_setter()

def work_order_customize_field():
        work_order_custom_field = {
            "Work Order": [
                dict(fieldname='ts_work_order_status', 
                label='Linked Work Order',
                fieldtype='Table',
                options='TS Work Order Status',
                insert_after='company',
                read_only=1
                ),
                dict(fieldname='ts_parent_work_order',
                    label='Parent WorkOrder',
                    fieldtype='Data',
                    insert_after='ts_work_order_status',
                    read_only=1)
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
def work_card_property_setter():                
    make_property_setter("Work Order", "sales_order", "hidden", 1, "Check")
    make_property_setter("Work Order", "project", "hidden", 1, "Check")
    make_property_setter("Work Order", "settings_section", "hidden", 1, "Check")
    make_property_setter("Work Order", "warehouses", "hidden", 1, "Check")
    make_property_setter("Work Order", "time", "hidden", 1, "Check")
    make_property_setter("Work Order", "more_info", "hidden", 1, "Check")

