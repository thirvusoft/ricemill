import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def operation_customize_field():
    custom_fields = {
        "Operation": [
            dict(fieldname='section_break_opration',
            label='Operation',
            fieldtype='Section Break',
            insert_after='quality_inspection_template',
            collapsible=1),
            dict(fieldname="grading_operation",
            label="Grading",
            fieldtype="Check",
            insert_after="section_break_opration",
            ),

            dict(fieldname="capacity_operation",
            label="Max Capacity",
            fieldtype="Data",
            insert_after="grading_operation",
            depends_on="eval:doc.grading_operation==1",
            mandatory_depends_on="eval:doc.grading_operation==1"
            ),
            dict(fieldname="capacity_exceeds",
            label="When Capacity exceeds",
            fieldtype="Select",
            options="\nAllow\nBlock",
            insert_after="capacity_operation",
            depends_on="eval:doc.grading_operation==1",
            mandatory_depends_on="eval:doc.grading_operation==1"
            ),
            dict(fieldname="shoking_operation",
            label="Shoking",
            fieldtype="Check",
            insert_after="capacity_exceeds",
            ),
            dict(fieldname="boiling_operation",
            label="Boiling",
            fieldtype="Check",
            insert_after="shoking_operation",
            ),
            dict(fieldname="dryer_operation",
            label="Dryer",
            fieldtype="Check",
            insert_after="boiling_operation",
            ),
            dict(fieldname="hulling_operation",
            label="Hulling",
            fieldtype="Check",
            insert_after="dryer_operation",
            )
            
            ]
            }

    create_custom_fields(custom_fields)

