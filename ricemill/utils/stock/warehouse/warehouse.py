import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def create_warehouse_fields():
    custom_fields={
        "Warehouse":[
            dict(fieldname="section_break_228", fieldtype="Section Break", insert_after="disabled"),
            dict
                (fieldname='section_break_1',  label='Warehouse Capacity',
                fieldtype='Section Break', insert_after='section_break_228', read_only=0),

            dict(fieldname='capacity', label='Need Capacity Restrictions',
                fieldtype='Check', insert_after='section_break_1', read_only=0,),

            dict(fieldname='warehouse_capacity', label='Warehouse Capacity',
                fieldtype='Float', insert_after='capacity', read_only=0, depends_on='eval:doc.capacity==1'),

            dict(fieldname='block', label='Block',
                fieldtype='Check', insert_after='warehouse_capacity', read_only=0, depends_on='eval:doc.capacity==1'),
            
            dict(fieldname='message', label='Message',
                fieldtype='Check', insert_after='block', read_only=0, depends_on='eval:doc.capacity==1'),
            
            dict(fieldname='column_break_01', label='',
                fieldtype='Column Break', insert_after='message', read_only=0),

            dict(fieldname='uom_warehouse_capacity', label='UOM',
                fieldtype='Link', insert_after='column_break_01',options='UOM', read_only=0, depends_on='eval:doc.capacity==1'),


            dict(fieldname='section_break_2', label='Batch Configuration',
                fieldtype='Section Break', insert_after='column_break_01', read_only=0, depends_on='eval:doc.message==1'),

            dict(fieldname='batch', label='Batch',
                fieldtype='Heading', insert_after='section_break_2', read_only=0),
            
            dict(fieldname='batch_not_allow', label='Batch Not Allow',
                fieldtype='Check', insert_after='batch', read_only=0),
            
            dict(fieldname='allow_as_batch', 
                label='Allow as',
                fieldtype='Select',
                options='\nMerge with Existing Batch\nMerge with Incoming Batch\nSeparate Batch',
                insert_after='batch_not_allow', 
                read_only=0,
                depends_on='eval:doc.batch_not_allow==0'),


            dict(fieldname='column_break_00', label='',
                fieldtype='Column Break', insert_after='allow_as_batch', read_only=0),
            
            dict(fieldname='different_item', label='Different Item',
                fieldtype='Heading', insert_after='column_break_00', read_only=0),
            
            dict(fieldname='_different_item_not_allow', label='Different Item Not Allow',
                fieldtype='Check', insert_after='different_item', read_only=0),
            
            dict(fieldname='allow_as_item', 
                label='Allow as',
                fieldtype='Select',
                options='\nMerge with Existing Item\nMerge with Incoming Item\nSeparate Item' ,
                insert_after='_different_item_not_allow', 
                read_only=0,
                depends_on='eval:doc._different_item_not_allow==0'),

            
        ]
    }

    create_custom_fields(custom_fields)
    
