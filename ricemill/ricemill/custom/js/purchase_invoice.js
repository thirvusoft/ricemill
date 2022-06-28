frappe.ui.form.on("Purchase Invoice",{
    "ts_purchase_partner":function(frm){
        console.log("hyy");
cur_frm.set_value('total_commission', (frm.doc.ts_commission_rate/100)*frm.doc.grand_total)
console.log(frm.doc.total_commission);
    }
})




