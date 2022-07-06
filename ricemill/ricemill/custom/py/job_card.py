import frappe
from frappe.utils import get_link_to_form
import json
from frappe.utils.data import flt


@frappe.whitelist()
def check_quality_inspection(doc):
    doc = json.loads(doc)
    operation = frappe.get_all("Operation", {'name': doc['operation']}, [
                               "grading", "soaking", "boiling", "dryer", "hulling"])
    opr = ""
    for i in operation[0]:
        if operation[0][i] == 1:
            opr = i
            break
    if opr == "":
        frappe.throw("Select a Valid Operation  " +
                     get_link_to_form("Operation", doc['operation']))
    inspection_req = frappe.get_value("Item", doc['production_item'], opr)
    if inspection_req:
        quality_inspection = frappe.get_value(
            "Quality Inspection", {'reference_name': doc['name']}, "name")
        if not quality_inspection:
            frappe.throw("Quality Inspection is Missing")


def before_submit(doc, action):
    jc_rej = sum([flt(i) for i in frappe.get_all("Quality Inspection", {
                 'reference_name': doc.name, 'status': 'Rejected'}, pluck='accepted_rejected_qty')])
    if jc_rej:
        frappe.msgprint(f'The Rejected item Quantity {jc_rej}')
