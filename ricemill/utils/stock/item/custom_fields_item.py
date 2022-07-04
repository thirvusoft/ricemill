from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def item_field_customize():
    custom_fields = {
        "Item": [
            dict(fieldname="grading",
                 label="Grading",
                 fieldtype="Check",
                 insert_after="inspection_required_before_purchase",
                 ),
            dict(fieldname="quality_inspection_template_2",
                 label="Quality Inspection Template",
                 fieldtype="Link",
                 options="Quality Inspection Template",
                 insert_after="grading",
                 depends_on="eval:doc.grading==1"
                 ),

            dict(fieldname="soaking",
                 label="Soaking",
                 fieldtype="Check",
                 insert_after="quality_inspection_template_2",
                 ),
            dict(fieldname="quality_inspection_template_3",
                 label="Quality Inspection Template",
                 fieldtype="Link",
                 options="Quality Inspection Template",
                 insert_after="soaking",
                 depends_on="eval:doc.soaking==1"
                 ),

            dict(fieldname="boiling",
                 label="Boiling",
                 fieldtype="Check",
                 insert_after="quality_inspection_template_3",
                 ),
            dict(fieldname="quality_inspection_template_4",
                 label="Quality Inspection Template",
                 fieldtype="Link",
                 options="Quality Inspection Template",
                 insert_after="boiling",
                 depends_on="eval:doc.boiling==1"
                 ),
            dict(fieldname="dryer",
                 label="Dryer",
                 fieldtype="Check",
                 insert_after="quality_inspection_template_4",
                 ),
            dict(fieldname="quality_inspection_template_5",
                 label="Quality Inspection Template",
                 fieldtype="Link",
                 options="Quality Inspection Template",
                 insert_after="dryer",
                 depends_on="eval:doc.dryer==1"
                 ),

            dict(fieldname="hulling",
                 label="Hulling",
                 fieldtype="Check",
                 insert_after="quality_inspection_template_5",
                 ),
            dict(fieldname="quality_inspection_template_6",
                 label="Quality Inspection Template",
                 fieldtype="Link",
                 options="Quality Inspection Template",
                 insert_after="hulling",
                 depends_on="eval:doc.hulling==1"
                 ),

            dict(fieldname="section",
                 label="Item Available Period",
                 fieldtype="Section Break",
                 insert_after="image",
                 collapsible=1,
                 ),
            dict(fieldname="item_season",
                 label="Item Available Period",
                 fieldtype="Table",
                 options="TS Item Available Period",
                 insert_after="section",
                 ),
            dict(fieldname="minimum_stock_level",
                 label="Minimum Stock Level",
                 fieldtype="Float",
                 reqd=1,
                 insert_after="is_item_from_hub",
                 ),
        ],
    }
    create_custom_fields(custom_fields)


def property_setter_item_field():
    make_property_setter("Item", "inspection_criteria",
                         "label", "Quality Inspection Criteria", ""),
    make_property_setter("Item", "quality_inspection_template",
                         "depends_on", "inspection_required_before_purchase", "")
