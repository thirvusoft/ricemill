import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import json

def purchase_invoice_customize_field():
    purchase_invoice_customize_field = {
        "Purchase Invoice": [
            dict(fieldname="section_break1",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='items'
                 ),
            dict(fieldname="last_purchase",
                 label='Select Last Purchase Limit',
                 fieldtype='Select',
                 insert_after='section_break1',
                 options="5\n4\n3\n2\n1",
                 default="3"
                 ),
            dict(fieldname="ts_last_purchase_item",
                 label='Last Purchase Item',
                 fieldtype='Table',
                 options="Last Purchase Item List Details",
                 read_only=1,
                 insert_after='last_purchase'
                 ),
            dict(fieldname="section_break2",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='ts_last_purchase_item'
                 ),
        ],
        "Purchase Invoice Item": [
            dict(fieldname="batch_configuration",
                 label='Batch Configuration',
                 fieldtype='Select',
                 options='\nMerge with Existing Batch\nMerge with Incoming Batch\nSeparate Batch',
                 depends_on="eval:doc.batch_configuration == 'Merge with Existing Batch' || doc.batch_configuration == 'Merge with Incoming Batch' || doc.batch_configuration == 'Separate Batch' ",
                 read_only=0,
                 ),
            dict(fieldname="select_batch",
                 label='Select Batch',
                 fieldtype='Link',
                 options="Batch",
                 insert_after='batch_configuration',
                 mandatory_depends_on="eval:doc.batch_configuration == 'Merge with Existing Batch' || doc.batch_configuration == 'Merge with Incoming Batch' ",
                 depends_on=	"eval:doc.batch_configuration == 'Merge with Existing Batch' || doc.batch_configuration == 'Merge with Incoming Batch' "
                 
                 ),
            dict(fieldname="item_conversion_type",
                 label='Item Conversion Type',
                 fieldtype='Select',
                 options='\nMerge with Existing Item\nMerge with Incoming Item\nSeparate Item' ,
                 read_only_depends_on="",
                 depends_on= "eval:doc.item_conversion_type == 'Merge with Existing Item' || doc.item_conversion_type == 'Merge with Incoming Item' ",
                 ),
            dict(fieldname="ts_select_item_conversion",
                 label='Select Item Conversion',
                 fieldtype='Select',
                 options="",
                 insert_after='item_conversion_type',
                 mandatory_depends_on="eval:doc.item_conversion_type == 'Merge with Existing Item' || doc.item_conversion_type == 'Merge with Incoming Item' ",
                 depends_on=	"eval:doc.item_conversion_type == 'Merge with Existing Item' || doc.item_conversion_type == 'Merge with Incoming Item' "
                 
                 ),
            dict(fieldname="select_item_conversion_batch",
                 label='Select Item Conversion Batch',
                 fieldtype='Link',
                 options="Batch",
                 insert_after='ts_select_item_conversion',
                 mandatory_depends_on="eval:doc.item_conversion_type == 'Merge with Existing Item' || doc.item_conversion_type == 'Merge with Incoming Item' ",
                 depends_on=	"eval:doc.item_conversion_type == 'Merge with Existing Item' || doc.item_conversion_type == 'Merge with Incoming Item' ",
                 
                 )
        ]
    }

    create_custom_fields(purchase_invoice_customize_field)