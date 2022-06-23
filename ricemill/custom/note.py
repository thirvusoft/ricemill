from dataclasses import fields
import frappe
from frappe.utils import (add_days, today)
def remainder_note():
    date = add_days(today(),7)
    item = frappe.get_all("TS Item Available Period", filters={'from_date':["between",(today(),date)]},fields=["parent","territory"])
    territory={}
    for i in item:
        if(i['parent'] in territory.keys()):
            territory[i["parent"]].append(i["territory"])  
        else:
            territory[i['parent']]= [i['territory']]
    parent=[i["parent"] for i in item]
    item_name = frappe.get_all("Item",filters={'name':['in',parent]},fields=['item_name','name'])
    content = "It's a Time for Buying an Item"
    for i  in item_name:
        content+=f"<p>{i['item_name']} Available in {(', ').join(territory[i['name']])}</p>"
        
    doc = frappe.get_value("Note",{"expire_notification_on":date},"name")
    if doc:
        note=frappe.get_doc("Note",doc)
    else :
        note = frappe.new_doc("Note")
    note.update({
    "title":"Remainder",
    "public":1,
    "notify_on_login":1,
    "expire_notification_on":date,
    "content":content,   
    })
    note.save(ignore_permissions=True)
    frappe.db.commit()

