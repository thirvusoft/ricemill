from cProfile import label
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def purchase_receipt_customize_field():
    purchase_receipt_customize_field = {
        "Purchase Receipt": [
            dict(fieldname="section_break1",
                 label='Last Purchase Item List Details',
                 fieldtype='Section Break',
                 insert_after='items'
                 ),
            dict(fieldname="last_purchase_item",
                 label='Last Purchase Item',
                 fieldtype='Link',
                 options="Item",
                 read_only=1,
                 insert_after='section_break1'
                 ),
            dict(fieldname="column_break11",
                 fieldtype='Column Break',
                 insert_after='last_purchase_item'
                 ),
            dict(fieldname="last_purchase_supplier",
                 label='Last Purchase Supplier',
                 fieldtype='Link',
                 options="Supplier",
                 read_only=1,
                 insert_after='column_break11'
                 ),
            dict(fieldname="column_break12",
                 fieldtype='Column Break',
                 insert_after='last_purchase_supplier'
                 ),
            dict(fieldname="last_purchase_rate",
                 label='Last Purchase Rate',
                 fieldtype='Currency',
                 read_only=1,
                 insert_after='column_break12'
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
                 read_only=0,
                 ),
            dict(fieldname="select_batch",
                 label='Select Batch',
                 fieldtype='Link',
                 options="Batch",
                 mandatory_depends_on="eval:doc.batch_configuration == 'Merge with Existing Batch' || doc.batch_configuration == 'Merge with Incoming Batch' ",
                 depends_on=	"eval:doc.batch_configuration == 'Merge with Existing Batch' || doc.batch_configuration == 'Merge with Incoming Batch' "
                 
                 )
        ]
    }

    create_custom_fields(purchase_receipt_customize_field)
import frappe
def batch_configuration(self,action):
     for i in self.items:
          warehouse=frappe.get_doc("Warehouse",i.warehouse)
          warehouse_qty=sum(frappe.db.get_all("Bin",pluck="actual_qty" ,filters={"warehouse":i.warehouse}))
          if warehouse.warehouse_capacity <= warehouse_qty:
               if warehouse.message == 1:
                    if warehouse.allow_as_batch == "Merge with Existing Batch":
                         i.batch_configuration = "Merge with Existing Batch"
                    elif warehouse.allow_as_batch == "Merge with Incoming Batch":
                         i.batch_configuration = "Merge with Incoming Batch"
                    elif warehouse.allow_as_batch == "Separate Batch":
                         i.batch_configuration = "Separate Batch"
                    else:
                         i.batch_configuration = warehouse.allow_as_batch

