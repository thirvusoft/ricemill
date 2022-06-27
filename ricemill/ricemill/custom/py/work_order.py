import frappe
def check_quality_inspection(doc,actions):
    quality_inspection=frappe.get_value("Quality Inspection",{'reference_name':doc.name},"name")
    if not quality_inspection:
        frappe.throw ("Quality Inspection is Missing")
