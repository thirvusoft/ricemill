frappe.ui.form.on('Purchase Invoice Item', {
    item_code: function (frm, cdt, cdn) {
        let p = locals[cdt][cdn]
        if (p.item_code) {
            frappe.call({
                method: "ricemill.ricemill.custom.py.purchase_invoice.get_last_purchase_invoice_details",
                args: {
                    item_code: p.item_code
                },
                callback: function (r) {
                    if (r.message.length) {
                        cur_frm.set_value("last_purchase_item", p.item_code)
                        cur_frm.set_value("last_purchase_rate", r.message[2])
                        cur_frm.set_value("last_purchase_supplier", r.message[1])
                        frm.refresh();
                        console.log(r.message)
                    }
                }
            })
        }
    }
})

