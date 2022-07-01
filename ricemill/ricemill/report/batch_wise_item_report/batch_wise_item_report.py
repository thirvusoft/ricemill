import re
import frappe
import json
from frappe import _

def execute(filters=None):
	item_name = filters.get("item_name")
	batch_no = filters.get("batch_no")
	conditions = '''where sed.t_warehouse is null and sed.docstatus = 1'''
	if(type(item_name) is str):
		conditions += " and sed.item_code = '{0}' ".format(item_name)
	if(type(batch_no) is str):
		conditions += " and sed.batch_no = '{0}' ".format(batch_no)
	s_data = frappe.db.sql(""" SELECT 
									sed.item_code as raw_item_code,
									sed.item_name as raw_item,
									sed.batch_no as purchase_batch_no,
									b.reference_doctype as ref_docType,
									b.reference_name as ref_voucher,
									sed.basic_amount as rate,										
									sed.parent
								FROM `tabStock Entry Detail` as sed RIGHT JOIN `tabBatch` as b ON sed.batch_no = b.name
								{0}
							""".format(conditions),as_dict=1)
	parent=[i["parent"] for i in s_data]
	cond = ""
	if len(parent)>1:
		cond += " and sed.parent in {0} ".format(tuple(parent))
	elif len(parent)==1:
		cond += " and sed.parent = '{0}'".format(parent[0])
	else:
		cond +=" "
	t_data = frappe.db.sql(""" SELECT 
									sed.item_code,
									sed.item_name as item_name,
									sed.batch_no as converted_batch,
									sed.amount as output_amount,
									sed.additional_cost as total_exp,
									sed.parent , sed.s_warehouse
								FROM `tabStock Entry Detail` as sed
								where  sed.docstatus = 1 and (sed.s_warehouse is NULL or sed.is_finished_item = 1) {0} 
							""".format(cond),as_dict=1)
	if len(parent)==0:
		t_data=[]
	for i in range (len(t_data)):
		for j in range (len(s_data)):
			if(t_data[i].parent == s_data[j].parent):
				t_data[i]["raw_item"]=s_data[j].raw_item
				t_data[i]["purchase_batch_no"]=s_data[j].purchase_batch_no
				t_data[i]["ref_docType"]=s_data[j].ref_docType
				t_data[i]["ref_voucher"]=s_data[j].ref_voucher
				t_data[i]["rate"]=s_data[j].rate
	columns, data = get_columns(),t_data
	return columns, data
def get_columns():
	columns = [
		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "raw_item",
			"width": 100
		},
		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "item_name",
			"width": 100
		},
		{
			"label": _("Purchase Batch No"),
			"fieldtype": "Link",
			"fieldname": "purchase_batch_no",
			"options":"Batch",
			"width": 150
		},
		{
			"label": _("Converted Batch"),
			"fieldtype": "Link",
			"fieldname": "converted_batch",
			"options": "Batch",
			"width": 150
		},
		{
			"label": _("Reference DocType"),
			"fieldtype": "Data",
			"fieldname": "ref_docType",
			"width": 150
		},
		{
			"label": _("Reference Voucher"),
			"fieldtype": "Data",
			"fieldname": "ref_voucher",
			"width": 200
		},
		{
			"label": _("Rate"),
			"fieldtype": "Float",
			"fieldname": "rate",
			"width": 120
		},
		{
			"label": _("Total Expense"),
			"fieldtype": "Float",
			"fieldname": "total_exp",
			"width": 120
		},
		{
			"label": _("Output Amount"),
			"fieldtype": "Float",
			"fieldname": "output_amount",
			"width": 120
		},
	]
	return columns
