frappe.ui.form.on('Purchase Order Item', {
    item_code: function (frm, cdt, cdn) {
        let p = locals[cdt][cdn]
        if (p.item_code) {
            frappe.call({
                method: "ricemill.ricemill.custom.py.purchase.get_last_purchase_details",
                args: {
                    item_code: p.item_code
                },
                callback: function (r) {
                    cur_frm.set_value("last_purchase_item", p.item_code)
                    cur_frm.set_value("last_purchase_rate", r.message[2])
                    cur_frm.set_value("last_purchase_supplier", r.message[1])
                    frm.refresh();
                }
            })
        }
    }
})

