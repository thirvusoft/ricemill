var rows;
frappe.ui.form.on('Purchase Order', {
    setup: function (frm, cdt, cdn) {
        rows = locals[cdt][cdn]
    },
})
frappe.ui.form.on('Purchase Order Item', {
    item_code: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn]
        if (row.item_code) {
            frappe.call({
                method: "ricemill.ricemill.custom.py.purchase_invoice.get_last_purchase_invoice_details",
                args: {
                    item_code: row.item_code,
                    last_purchase: rows.last_purchase
                },
                callback: function (r) {
                    if (r.message.length) {
                        cur_frm.set_value("ts_last_purchase_item",r.message )
                        frm.refresh();
                    }
                    else{
                        cur_frm.set_value("ts_last_purchase_item",[] )
                        frm.refresh();
                    }
                }
            })
        }
    }
})