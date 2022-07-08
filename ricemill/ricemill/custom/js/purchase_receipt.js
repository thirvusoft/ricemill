var rows;
frappe.ui.form.on('Purchase Receipt', {
    setup: function (frm, cdt, cdn) {
        rows = locals[cdt][cdn]
    },
    last_purchase: function(frm,cdt,cdn){
        if (rows.items) {
            for(var i=rows.items.length-1;i<rows.items.length;i++){
                changes(frm,rows.items[i].item_code)
            }
        }
    },
    set_warehouse: function(frm){
        frm.doc.items.forEach(element => {
            set_warehouse_validation_field(frm,element.doctype,element.name)
        });
    }
})
frappe.ui.form.on('Purchase Receipt Item', {
    item_code: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn]
        if (row.item_code) {
            changes(frm,row.item_code)
        }
        set_warehouse_validation_field(frm,cdt,cdn)
    },
    'warehouse': function(frm,cdt,cdn){
        set_warehouse_validation_field(frm,cdt,cdn)
    }
})
function changes(frm,item_code){
    if(item_code){
    frappe.call({
        method: "ricemill.ricemill.custom.py.purchase_invoice.get_last_purchase_invoice_details",
        args: {
            item_code:item_code,
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
function select_item_option(frm,cdt,cdn){
    let row = locals[cdt][cdn]
    var option=[]
    frappe.db.get_list('Bin',
		{fields:['item_code']},{filters: {warehouse: row.warehouse}}).then((res) => {
            for(var i=0;i<res.length;i++){
                option.push(res[i].item_code);
            }
            var df = frappe.meta.get_docfield("Purchase Receipt Item","ts_select_item_conversion", row.name);
            df.options = option;
            frm.refresh(row.ts_select_item_conversion);
		});
}
function set_warehouse_validation_field(frm, cdt, cdn){
    let row = locals[cdt][cdn]
    if(row.item_code){
    frappe.db.get_list("Item", {filters:{'name':row.item_code},fields:['has_batch_no']}).then( (batch)=>{
        if(batch[0].has_batch_no === 1){
            if(row.warehouse){
                frappe.db.get_list("Warehouse",{filters:{'name':row.warehouse},
                    fields:['message', 'batch_not_allow', 'allow_as_batch', '_different_item_not_allow','allow_as_item']}).then( (r)=>{
                        let data = r[0]
                        let batch_configuration = '', item_conversion_type = '';
                        if(data.message === 1){
                            if(data.batch_not_allow === 1){
                                if(data.allow_as_batch === "Merge with Existing Batch"){
                                    batch_configuration = "Merge with Existing Batch"
                                }
                                if(data.allow_as_batch === "Merge with Incoming Batch"){
                                    batch_configuration = "Merge with Incoming Batch"
                                }
                                if(data.allow_as_batch === "Separate Batch"){
                                    batch_configuration = "Separate Batch"
                                }
                                else{
                                    batch_configuration = data.allow_as_batch
                                }
                                frappe.model.set_value(cdt, cdn, 'batch_configuration', batch_configuration)
                                frm.refresh();
                            }
                            else{if(data._different_item_not_allow === 1){
                                if(data.allow_as_item === "Merge with Existing Item"){
                                    item_conversion_type = "Merge with Existing Item"
                                }
                                if(data.allow_as_item === "Merge with Incoming Item"){
                                    item_conversion_type = "Merge with Incoming Item"
                                }
                                if(data.allow_as_item === "Separate Item"){
                                    item_conversion_type = "Separate Item"
                                }
                                // else{
                                //     item_conversion_type = data.allow_as_item
                                // }
                                frappe.model.set_value(cdt, cdn, 'item_conversion_type', item_conversion_type)
                                frm.refresh()
                            }}
                        }
                    })
                }
        select_item_option(frm,cdt,cdn)
        }
    })   } 
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
        if(!item.item_code) {
            frappe.throw(__("Please enter Item Code to get Batch Number"));
        } else {
                var filters = {
                    'item_code': item.ts_select_item_conversion,
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
    });
}
})

