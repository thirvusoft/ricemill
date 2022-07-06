from curses import KEY_MARK
import frappe
from frappe.utils import get_link_to_form
import json
from frappe.utils.data import flt
@frappe.whitelist()
def check_quality_inspection(doc):
    doc=json.loads(doc)
    operation=frappe.get_all("Operation",{'name':doc['operation']},["grading","soaking","boiling","dryer","hulling"])
    opr=""
    for i in operation[0]:
        if operation[0][i]==1:
            opr=i
            break
    if opr=="":frappe.throw("Select a Valid Operation  "+ get_link_to_form("Operation",doc['operation']))
    inspection_req=frappe.get_value("Item",doc['production_item'],opr)
    if inspection_req:
        quality_inspection=frappe.get_value("Quality Inspection",{'reference_name':doc['name']},"name")
        if not quality_inspection:
            frappe.throw ("Quality Inspection is Missing")
def before_submit(doc,action):
    jc_rej=sum([flt(i) for i in frappe.get_all("Quality Inspection",{'reference_name':doc.name,'status':'Rejected'},pluck='accepted_rejected_qty')])
    if jc_rej:
        frappe.msgprint(f'The Rejected item Quantity {jc_rej}')

@frappe.whitelist()
def repack_dialog(item,operation,qty):
    opr  = frappe.db.get_value("Operation", operation, 'hulling')
    if(not opr):return
    else:
        uom = frappe.get_all("UOM Conversion Detail", {'parent':item},['uom','conversion_factor'])
        fields=[]
        stock_uom = frappe.get_value("Item", item, 'stock_uom')
        for i in range(len(uom)):
            fields.append({'fieldname':f'uom{i+1}','label':uom[i]['uom'],'fieldtype':'Link','default':uom[i]['uom'],'read_only':1})
            fields.append({'fieldtype':'Column Break','fieldname':f'column{i+1}'})
            fields.append({'fieldtype':'Float','fieldname':f'conv{i+1}','default':uom[i]['conversion_factor'],'read_only':1, 'hidden':1})
            fields.append({'fieldtype':'Column Break','fieldname':f'column1{i+1}'})
            fields.append({'fieldtype':'Float','fieldname':f'qty{i+1}','default':0,'description':f"Enter QTY in {stock_uom}"})
            fields.append({'fieldtype':'Section Break','fieldname':f'section{i+1}'})
        fields+=[
            {'fieldname':f'default_uom','label':"Stock UOM",'fieldtype':'Link','default':stock_uom,'read_only':1},
            {'fieldtype':'Column Break','fieldname':'column_1'},
            {'fieldtype':'Float','label':"Total QTY",'fieldname':'total_qty','default':qty,'read_only':1},
            {'fieldtype':'Column Break','fieldname':f'column_2'},
            {'fieldtype':'Float','label':"Remaining QTY",'fieldname':'remaining_qty','default':qty},
        ]
        return fields, len(uom)

@frappe.whitelist()
def make_repack(items, length, work_order_id, purpose, qty=0, sw=None, tw = None):
    items = json.loads(items)
    uom,conv,qnty = separate_items_data(items, length)
    work_order = frappe.get_doc("Work Order", work_order_id)
    se_item = ''
    se_item = frappe.get_doc("Item",work_order.production_item)
    parent_wo = frappe.get_value("Work Order", work_order_id, 'ts_parent_work_order')
    se_name = frappe.get_value("Stock Entry", {'ts_work_order':parent_wo},'name')
    batch_no = frappe.get_value("Batch",{'reference_doctype':'Stock Entry','reference_name':se_name},'name')
    scrap_item = ''
    stock_entry = frappe.new_doc("Stock Entry")
    stock_entry.ts_work_order = work_order_id
    stock_entry.purpose = purpose
    stock_entry.company = work_order.company
    items ={ 
        "item_code":se_item.item_code,
        "item_group": se_item.item_group, 
        "item_name":se_item.item_name, 
        "qty": qty , 
        "uom":se_item.stock_uom, 
        "conversion_factor": 1,
        "batch_no": batch_no,
        "s_warehouse" : sw
         }
    stock_entry.append("items", items)

    ## Add Repacked item in different uoms
    for i in range(len(qnty)):
        items ={ 
        "item_code":se_item.item_code,
        "item_group": se_item.item_group, 
        "item_name":se_item.item_name, 
        "qty": qnty[i] , 
        "uom":uom[i], 
        "conversion_factor": conv[i],
        "t_warehouse": tw,
        "is_finished_item": 1
         }
        stock_entry.append("items", items)
    # stock_entry.set_serial_no_batch_for_finished_good()
    
    from erpnext.manufacturing.doctype.bom.bom import add_additional_cost
    add_additional_cost(stock_entry, work_order)
    
    job_card = frappe.get_all("Job Card", filters={'work_order':work_order_id},pluck = 'name')[0]
    jc_doc = frappe.get_doc("Job Card", job_card)
    scrap_item = jc_doc.scrap_items
    for i in scrap_item:
        items ={ 
        "item_code":i.item_code,
        "item_group": frappe.get_value("Item", i.item_code, 'item_group'), 
        "item_name":i.item_name, 
        "qty": i.stock_qty , 
        "uom":i.stock_uom, 
        "conversion_factor": 1,
        "is_scrap_item": 1,
        "t_warehouse" : tw,
        }
        if(purpose != 'Manufacture'):items['batch_no'] = batch_no
        stock_entry.append("items", items)
    stock_entry.project = work_order.project
    stock_entry.set_stock_entry_type()
    stock_entry.insert(ignore_mandatory=True, ignore_permissions=True)
    stock_entry.submit()
    jc_doc.submit()
    from ricemill.ricemill.custom.py.workorder import change_status
    change_status(work_order_id)
    frappe.db.commit()
    return stock_entry.as_dict()


def separate_items_data(items, length):
    uom, conv, qty= [], [], []
    for i in range(1, int(length)+1):
        if(items[f"qty{i}"] > 0):
            uom.append(items[f"uom{i}"])
            conv.append(items[f"conv{i}"])
            qty.append(items[f"qty{i}"])
    return uom,conv,qty