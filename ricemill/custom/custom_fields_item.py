from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe
def customize():
        custom_fields = {
        "Item": [
            dict(fieldname="on_purchase",
            label="On Purchase",
            fieldtype="Check",
            insert_after="quality_inspection_template",
            ),
            dict(fieldname="quality_inspection_template_1",
            label="Quality Inspection Template",
            fieldtype="Link",
            options="Quality Inspection Template",
            insert_after="on_purchase",
            depends_on="eval:doc.on_purchase==1"
            ),
            dict(fieldname="grading",
            label="Grading",
            fieldtype="Check",
            insert_after="quality_inspection_template_1",
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
        ],
        }
        Item=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Item",
        'property':"label",
        'field_name':"inspection_criteria",
        "value":"Quality Inspection Criteria"
    })
        Item=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Item",
        'property':"hidden",
        'property_type':"Check",
        'field_name':"quality_inspection_template",
        "value":1
    })
        Item=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field':"DocField",
        'doc_type': "Item",
        'property':"hidden",
        'property_type':"Check",
        'field_name':"inspection_required_before_delivery",
        "value":1
    })
        Item=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field':"DocField",
        'doc_type': "Item",
        'property':"hidden",
        'property_type':"Check",
        'field_name':"inspection_required_before_purchase",
        "value":1
    })
        Item.save()
        create_custom_fields(custom_fields)


