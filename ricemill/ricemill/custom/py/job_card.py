import frappe
from frappe.utils import get_link_to_form
import json
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
