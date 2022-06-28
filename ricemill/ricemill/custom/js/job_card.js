frappe.ui.form.on("Job Card",{
   "refresh":function(frm){
    frm.add_custom_button(__("Quality Inspection(s)"), () => {
            let data = [];
            var item =cur_frm.doc.production_item
            const fields = [
                {
                    label: "Items",
                    fieldtype: "Table",
                    fieldname: "items",
                    cannot_add_rows: true,
                    in_place_edit: true,
                    data: data,
                    get_data: () => {
                        return data;
                    },
                    fields: [
                        {
                            fieldtype: "Data",
                            fieldname: "docname",
                            hidden: true
                        },
                        {
                            fieldtype: "Read Only",
                            fieldname: "item_code",
                            label: __("Item Code"),
                            in_list_view: true,
                            options: "Item",
                        },
                        {
                            fieldtype: "Read Only",
                            fieldname: "item_name",
                            label: __("Item Name"),
                            in_list_view: true
                        },
                        {
                            fieldtype: "Float",
                            fieldname: "qty",
                            label: __("Accepted Quantity"),
                            in_list_view: true,
                            read_only: true
                        },
                        {
                            fieldtype: "Float",
                            fieldname: "sample_size",
                            label: __("Sample Size"),
                            reqd: true,
                            in_list_view: true
                        },
                        {
                            fieldtype: "Data",
                            fieldname: "description",
                            label: __("Description"),
                            hidden: true
                        },
                        {
                            fieldtype: "Data",
                            fieldname: "serial_no",
                            label: __("Serial No"),
                            hidden: true
                        },
                        {
                            fieldtype: "Data",
                            fieldname: "batch_no",
                            label: __("Batch No"),
                            hidden: true
                        }
                    ]
                }
            ];
        
            const dialog = new frappe.ui.Dialog({
                title: __("Select Items for Quality Inspection"),
                fields: fields,
                primary_action: function () {
                    const data = dialog.get_values();
                    frappe.call({
                        method: "erpnext.controllers.stock_controller.make_quality_inspections",
                        args: {
                            doctype: frm.doc.doctype,
                            docname: frm.doc.name,
                            items: data.items
                        },
                        freeze: true,
                        callback: function (r) {
                            if (r.message.length > 0) {
                                if (r.message.length === 1) {
                                    frappe.set_route("Form", "Quality Inspection", r.message[0]);
                                } else {
                                    frappe.route_options = {
                                        "reference_type": frm.doc.doctype,
                                        "reference_name": frm.doc.name
                                    };
                                    frappe.set_route("List", "Quality Inspection");
                                }
                            }
                            dialog.hide();
                        }
                    });
                },
                primary_action_label: __("Create")
            });
        
            // frm.doc.items.forEach(item => {
                // if (!frm.doc.production_itemquality_inspection) {
                    let dialog_items = dialog.fields_dict.items;
                    dialog_items.df.data.push({
                        "docname": frm.doc.production_item,
                        "item_code": frm.doc.production_item,
                        "item_name": frm.doc.item_name,
                        // "qty": frm.doc.production_itemqty,
                        // "description": frm.doc.production_itemdescription,
                        // "serial_no": frm.doc.production_itemserial_no,
                        // "batch_no": frm.doc.production_itembatch_no
                    });
                    dialog_items.grid.refresh();
                // }
            // });
        
            data = dialog.fields_dict.items.df.data;
            if (!data.length) {
                frappe.msgprint(__("All items in this document already have a linked Quality Inspection."));
            } else {
                dialog.show();
            }
        }, __("Create"));
    
}

})
