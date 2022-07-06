# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        {
            "label": _("Posting Date"),
            "fieldtype": "Date",
            "fieldname": "posting_date",
            "width": 150
        },
        {
            "label": _("work_order"),
            "fieldtype": "Link",
            "fieldname": "work_order",
            "options": "Work Order",
            "width": 150
        },
        {
            "label": _("Job Card"),
            "fieldtype": "Link",
            "fieldname": "name",
            "options": "Job Card",
            "width": 150
        },
        {
            "label": _("Manufacture Qty"),
            "fieldtype": "Float",
            "fieldname": "total_completed_qty",
            "width": 150
        },
        {
            "label": _("Time Taken(mins)"),
            "fieldtype": "Float",
            "fieldname": "total_time_in_mins",
            "width": 150
        },
        {
            "label": _("Status"),
            "fieldtype": "Data",
            "fieldname": "status",
            "options": "Open\nWork In Progress\nMaterial Transferred\nOn Hold\nSubmitted\nCancelled\nCompleted",
            "default": "Open",
            "width": 150
        },
        {
            "label": _("Operation"),
            "fieldtype": "Link",
            "fieldname": "operation",
            "options": "Operation",
            "width": 150
        },
        {
            "label": _("Workstation"),
            "fieldtype": "Link",
            "fieldname": "workstation",
            "options": "Workstation",
            "width": 150
        },
    ]
    return columns


def get_data(filters):
    filter = {'status':['not in', ('Open', 'Cancelled')]}
    keys = list(filters.keys())
    if("job_card" in keys):
        filter["name"] = filters["job_card"]
    if("status" in keys):
        filter["status"] = filters["status"]
    if("from_date" in keys and "to_date" in keys):
        filter["posting_date"] = ["between",
                                  (filters["from_date"], filters["to_date"])]
    elif("from_date" in keys):
        filter["posting_date"] = [">=", filters["from_date"]]
    elif("to_date" in keys):
        filter["posting_date"] = [
            "<=", filters["to_date"]]
    result = frappe.db.get_all(
        "Job Card", filters=filter, fields=["posting_date", "work_order", "name", "total_completed_qty", "total_time_in_mins", "status", "operation", "workstation"])
    return result
