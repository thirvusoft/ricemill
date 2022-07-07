frappe.ui.form.on("Job Card", {
    "refresh": function (frm) {
        if (!frm.doc.employee.length) {
            frm.set_value('time_logs', [])
        }
        frm.add_custom_button(__(""), () => {
            let data = [];
            var item = frm.doc.production_item
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
            let dialog_items = dialog.fields_dict.items;
            frappe.db.get_list("BOM Item", { filters: { 'parent': frm.doc.bom_no }, fields: ["item_code", "item_name"] }).then((bom_item) => {
                bom_item.forEach((item) => {
                    dialog_items.df.data.push({
                        "docname": frm.doc.name,
                        "item_code": item.item_code,
                        "item_name": item.item_name,
                    });
                    dialog_items.grid.refresh();
                    data = dialog.fields_dict.items.df.data;
                    if (!data.length) {
                        frappe.msgprint(__("All items in this document already have a linked Quality Inspection."));
                    } else {
                        dialog.show();
                    }
                })
            })

        }, __("Create"));
        frappe.db.get_list("Operation", { fields: ['hulling'], filters: { 'name': cur_frm.doc.operation } }).then((value) => {
            if (value[0].hulling === 1) {
                frm.add_custom_button(__("Stock Entry"), () => {
                    frappe.call({
                        method: "ricemill.ricemill.custom.py.job_card.repack_dialog",
                        async: false,
                        freeze: true,
                        freeze_message: "Please wait...",
                        args: {
                            item: frm.doc.production_item,
                            operation: frm.doc.operation,
                            qty: frm.doc.total_completed_qty
                        },
                        callback: function (r) {
                            if (r.message[0]) {
                                let count = 0
                                var func = function () {
                                    var used_qty = 0;
                                    for (let i = 1; i <= r.message[1]; i++) {
                                        used_qty += d.fields_dict['qty' + i].value * d.fields_dict['conv' + i].value
                                    }
                                    d.fields_dict['remaining_qty'].value = d.fields_dict.total_qty.value - used_qty
                                    d.fields_dict['remaining_qty'].refresh()

                                }
                                r.message[0].forEach((data) => {
                                    if (data['fieldname'].indexOf('qty') >= 0 && data['fieldname'] != 'total_qty' && data['fieldname'] != 'remaining_qty') {
                                        r.message[0][count]['onchange'] = func
                                    }
                                    count += 1
                                })
                                var d = new frappe.ui.Dialog({
                                    title: "Repack details for hulling operation",
                                    fields: r.message[0],
                                    freeze: true,
                                    static: true,
                                    primary_action: function (data) {
                                        if (d.fields_dict.remaining_qty.value === 0 || d.fields_dict.remaining_qty.value === null) {
                                            frappe.call({
                                                method: "ricemill.ricemill.custom.py.job_card.make_repack",
                                                args: {
                                                    items: data,
                                                    length: r.message[1],
                                                    work_order_id: cur_frm.doc.work_order,
                                                    purpose: cur_frm.doc.ts_stock_entry_type,
                                                    qty: cur_frm.doc.total_completed_qty,
                                                    sw: cur_frm.doc.ts_source_warehouse,
                                                    tw: cur_frm.doc.ts_target_warehouse
                                                },
                                                callback(r) {
                                                    frappe.model.sync(r.message);
                                                    frappe.set_route('Form', r.message.doctype, r.message.name);
                                                }
                                            })
                                            d.hide();
                                        }
                                        else {
                                            frappe.throw("Remaining qty must be equal to zero")
                                        }
                                    }
                                })
                                d.show()
                            }
                        }
                    })
                }, __("Create"));
            }
        });
    }
});

