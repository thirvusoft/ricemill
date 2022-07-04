from ipaddress import collapse_addresses
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def customize():
    job_card_customize_field()
    job_card_property_setter()


def job_card_customize_field():
    job_card_customize_field = {
        "Job Card": [
            dict(fieldname="section_break1",
                 label='Stock Entry',
                 fieldtype='Section Break',
                 collapsible=1,
                 insert_after='batch_no'
                 ),
            dict(fieldname="ts_source_warehouse",
                 label='Source Warehouse',
                 fieldtype='Link',
                 options="Warehouse",
                 reqd=1,
                 insert_after='section_break1'
                 ),
            dict(fieldname="column_break1",
                 fieldtype='Column Break',
                 insert_after='ts_source_warehouse'
                 ),
            dict(fieldname="ts_target_warehouse",
                 label='Target Warehouse',
                 fieldtype='Link',
                 options="Warehouse",
                 reqd=1,
                 insert_after='column_break1'
                 ),
            dict(fieldname="column_break2",
                 fieldtype='Column Break',
                 insert_after='ts_target_warehouse'
                 ),
            dict(fieldname="ts_stock_entry_type",
                 label='Stock Entry Type',
                 fieldtype='Link',
                 options="Stock Entry Type",
                 reqd=1,
                 insert_after='column_break2'
                 ),
        ]
    }

    create_custom_fields(job_card_customize_field)


def job_card_property_setter():
    make_property_setter("Job Card", "more_information", "hidden", 1, "Check")
    make_property_setter("Job Card", "wip_warehouse", "reqd", 0, "Check")
    make_property_setter("Job Card", "more_information", "hidden", 1, "Check")
    make_property_setter("Job Card", "wip_warehouse", "reqd", 0, "Check")
    make_property_setter(
        "Job Card", "quality_inspection_template", "hidden", 1, "Check")
    make_property_setter("Job Card", "quality_inspection",
                         "hidden", 1, "Check")
    make_property_setter("Job Card", "project", "hidden", 1, "Check")
