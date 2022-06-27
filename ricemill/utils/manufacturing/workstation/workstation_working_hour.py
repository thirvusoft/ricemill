import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def workstation_customize_field():
    custom_fields = {
        "Workstation": [
            dict(fieldname='section_break_labour', label='Is Accountable',
                fieldtype='Section Break',insert_after='production_capacity'),
            dict(fieldname='ts_labour', label='Is Accountable',
                fieldtype='Table',options='TS Workstation Labour',insert_after='section_break_labour',reqd=1),
            dict(fieldname='ts_net_hour_rate', label='Net Hour Rate',
                fieldtype='Currency',description='per hour',insert_after='hour_rate_labour'),
            dict(fieldname='ts_wages_hour_based', label='Wages Based On',
                fieldtype='Select',insert_after='hour_rate_consumable',options="Hour rate\n Piece rate",translatable=0)
                ]
                }

    create_custom_fields(custom_fields)

