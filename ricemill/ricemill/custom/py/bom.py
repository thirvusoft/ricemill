import frappe


def validate(doc,action):
    src_wh, tar_wh = [], []
    for opr in doc.operations:
        src_wh.append(opr.source_warehouse)
        tar_wh.append(opr.target_warehouse)
    idx,message=[],''
    for i in range(1,len(src_wh)):
        if(src_wh[i]!=tar_wh[i-1]):
            idx.append(i+1)
    for i in idx:
        message+= f"<p><b>Row</b>: <b>{i-1}</b> and <b>{i}</b> Doesn't have same target warehouse and source warehouse.<p>"
    if(idx):
        frappe.throw(message)
    