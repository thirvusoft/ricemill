frappe.ui.form.on("Work Order",{
    on_submit: function(frm){
        frappe.call({
            method: "ricemill.ricemill.custom.py.workorder.get_link",
            args:{doc:frm.doc.name},
            callback(r){
                window.location.assign(r.message)
            }
        })
    },
    onload: function(frm){
        if(frm.doc.__unsaved || frm.doc.ts_parent_work_order){
            frm.set_df_property("ts_work_order_status",'hidden',1)
        }
        else{
            frm.set_df_property("ts_parent_work_order",'hidden',1)
            frappe.call({
                method: "ricemill.ricemill.custom.py.workorder.get_child_work_order_status",
                args: {parent: frm.doc.name},
                callback(r){
                    var docstatus= cur_frm.doc.docstatus
                    cur_frm.set_value("ts_work_order_status", r.message)
                    cur_frm.refresh()
                    if(docstatus == 1){
                    cur_frm.save('Update')
                    }
                    else{
                        cur_frm.save()
                    }
                }
            })

        }
    }
})