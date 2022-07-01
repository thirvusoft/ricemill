// Copyright (c) 2022, Thirvusoft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Manufacturing Status Report"] = {
	"filters": [
		{
			"fieldname": "job_card",
			"label": __("Job Card"),
			"fieldtype": "Link",
			"options": "Job Card",

		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nOpen\nWork In Progress\nMaterial Transferred\nOn Hold\nSubmitted\nCancelled\nCompleted",
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
		},
	]
};
