frappe.ui.form.on("Operation",{
    refresh:function(frm){
        cur_frm.fields_dict.grading.$input.on("click", function() {
            frm.set_value('soaking',0)
            frm.set_value('boiling',0)
            frm.set_value('dryer',0)
            frm.set_value('hulling',0)
        }),
        cur_frm.fields_dict.soaking.$input.on("click", function() {
            frm.set_value('grading',0)
            frm.set_value('boiling',0)
            frm.set_value('dryer',0)
            frm.set_value('hulling',0)
    }),
        cur_frm.fields_dict.boiling.$input.on("click", function() {
            frm.set_value('grading',0)
            frm.set_value('soaking',0)
            frm.set_value('dryer',0)
            frm.set_value('hulling',0)
    }),
        cur_frm.fields_dict.dryer.$input.on("click", function() {
            frm.set_value('grading',0)
            frm.set_value('soaking',0)
            frm.set_value('boiling',0)
            frm.set_value('hulling',0)
    }),        
        cur_frm.fields_dict.hulling.$input.on("click", function() {
            frm.set_value('grading',0)
            frm.set_value('soaking',0)
            frm.set_value('boiling',0)
            frm.set_value('dryer',0)
        })
    }
})
   

