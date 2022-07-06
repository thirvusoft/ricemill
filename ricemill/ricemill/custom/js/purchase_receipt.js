frappe.ui.form.on('Purchase Receipt Item', {
    item_code: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn]
        if (row.item_code) {
            frappe.call({
                method: "ricemill.ricemill.custom.py.purchase_invoice.get_last_purchase_invoice_details",
                args: {
                    item_code: row.item_code
                },
                callback: function (r) {
                    if (r.message) {
                        cur_frm.set_value("last_purchase_item", row.item_code)
                        cur_frm.set_value("last_purchase_rate", r.message[2])
                        cur_frm.set_value("last_purchase_supplier", r.message[1])
                        frm.refresh();
                    }
                }
            })
        }
        select_item_option(frm,cdt,cdn)
    },
    warehouse: function(frm,cdt,cdn){
        select_item_option(frm,cdt,cdn)
    }
});
function select_item_option(frm,cdt,cdn){
    let row = locals[cdt][cdn]
    var option=[]
    frappe.db.get_list('Bin',
		{fields:['item_code']},{filters: {warehouse: row.warehouse}}).then((res) => {
            for(var i=0;i<res.length;i++){
                option.push(res[i].item_code);
            }
		});
    var df = frappe.meta.get_docfield("Purchase Receipt Item","ts_select_item_conversion", row.name);
    df.options = option;
    frm.refresh(row.ts_select_item_conversion);

}
frappe.ui.form.on('Purchase Receipt', {
    setup: function(frm, cdt, cdn){
        frm.set_query('select_batch', 'items', function(frm, cdt, cdn) {
        var item = locals[cdt][cdn];
        if(!item.item_code) {
            frappe.throw(__("Please enter Item Code to get Batch Number"));
        } else {
                var filters = {
                    'item_code': item.item_code,
                    'posting_date': frappe.datetime.nowdate()
            
                }
            // User could want to select a manually created empty batch (no warehouse)
            // or a pre-existing batch
                filters["warehouse"] = item.warehouse || item.t_warehouse;
            return {
                query : "erpnext.controllers.queries.get_batch_no",
                filters: filters
            }
        }
    }),
    frm.set_query('select_item_conversion_batch','items', function(frm, cdt, cdn) {
        var item = locals[cdt][cdn];
        return {
            filters: {
                "item": item.ts_select_item_conversion,
            }
        };
    });
}
})

