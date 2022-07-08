from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def purchase_receipt_customize_field():
    purchase_receipt_customize_field = {
        "Purchase Receipt": [
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
            dict(fieldname="vechile_no",
                 label='Vechile No',
                 fieldtype='Data',
                 insert_after='supplier_delivery_note'
                 ),
        ],
        "Purchase Receipt Item": [
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

    create_custom_fields(purchase_receipt_customize_field)
import frappe
def batch_configuration(self,action):
     for i in self.items:
          warehouse=frappe.get_doc("Warehouse",i.warehouse)
          warehouse_qty=sum(frappe.db.get_all("Bin",pluck="actual_qty" ,filters={"warehouse":i.warehouse}))
          # if warehouse.warehouse_capacity <= warehouse_qty:
          if warehouse.message == 1:
               if warehouse.batch_not_allow == 1:
                    if warehouse.allow_as_batch == "Merge with Existing Batch":
                         i.batch_configuration = "Merge with Existing Batch"
                    elif warehouse.allow_as_batch == "Merge with Incoming Batch":
                         i.batch_configuration = "Merge with Incoming Batch"
                    elif warehouse.allow_as_batch == "Separate Batch":
                         i.batch_configuration = "Separate Batch"
                    else:
                         i.batch_configuration = warehouse.allow_as_batch
               elif warehouse._different_item_not_allow  == 1:
                    if warehouse.allow_as_item == "Merge with Existing Item":
                         i.item_conversion_type = "Merge with Existing Item"
                    elif warehouse.allow_as_item == "Merge with Incoming Item":
                         i.item_conversion_type = "Merge with Incoming Item"
                    elif warehouse.allow_as_item == "Separate Item":
                         i.item_conversion_type = "Separate Item"
                    else:
                         i.item_conversion_type = warehouse.allow_as_item