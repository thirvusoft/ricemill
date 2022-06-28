import frappe
def  calc_commission(doc,event):
    if doc.ts_account:
        if doc=='Sales Invoice':
            if not doc.sales_partner:
                frappe.throw('Enter Sales Person for commission')
        elif doc =='Purchase Invoice':
            if not doc.ts_purchase_partner:
                frappe.throw('Enter Purchase Person for commission')
        if  not doc.cost_center:
            frappe.throw("Please select Cost Center")
        else:
            doc.base_grand_total=(doc.grand_total - doc.total_commission)


def create_gl_entry(doc,event):
    gl_doc=frappe.new_doc('GL Entry')
    gl_doc.posting_date=doc.due_date
    gl_doc.account=doc.commission_account
    gl_doc.cost_center=doc.cost_center
    gl_doc.voucher_type=doc.doctype
    gl_doc.voucher_no=doc.name
    gl_doc.credit=doc.total_commission
    gl_doc.credit_in_account_currency=doc.total_commission
    gl_doc.save()
    gl_doc.submit()

