import frappe
def check_quality_inspection(doc,actions):

    operation=frappe.get_all("Operation",{"name":doc.operations[0].operation},["grading_operation","shoking_operation","boiling_operation","dryer_operation","hulling_operation"])
    print(operation)



    quality_inspection=frappe.get_value("Quality Inspection",{'reference_name':doc.name},"name")
    print(quality_inspection)
    if not quality_inspection:
        frappe.throw ("Quality Inspection is Missing")
    else :
        pass
