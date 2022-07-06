frappe.ui.form.on("Warehouse", {
	refresh: function(frm) {

                cur_frm.fields_dict.block.$input.on("click", function() {
                    frm.set_value('message', 0)
                    
                }),
                cur_frm.fields_dict.message.$input.on("click", function() {
                    frm.set_value('block', 0)
                    
                })
            
        }
})