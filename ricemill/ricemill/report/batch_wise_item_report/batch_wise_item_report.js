// Copyright (c) 2022, Thirvusoft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Batch Wise Item Report"] = {
	"filters": [
		{
			"fieldname":"item_name",
			"label":__("Item Name"),
			"fieldtype":"Link",
			"options":"Item",
			get_query: function() {
				return {
					filters: {
						'has_batch_no': 1
					}
				}
			}
		},
		{
			"fieldname":"batch_no",
			"label":__("Batch No"),
			"fieldtype":"Link",
			"options":"Batch",
			get_query: function() {
				var item_name = frappe.query_report.get_filter_value('item_name');
				if(item_name){
					return {
						filters: {
							'item': item_name
						}
					}
				}
			}
		},
	]
};
