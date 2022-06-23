import frappe
from frappe.utils import (add_days, today)
def remainder_note():
    date = add_days(today(),7)
    item = frappe.get_all("TS Item Available Period", filters={'from_date':["between",(today(),date)]}, pluck='parent')
    item_name = frappe.get_all("Item",filters={'name':['in',item]},pluck='item_name')
    content = ""
    for i  in item_name:
        content+=f"<p>Item Name: {i}</p>"
    doc = frappe.get_value("Note",{"expire_notification_on":date},"name")
    if doc:
        note=frappe.get_doc("Note",doc)
    else :
        note = frappe.new_doc("Note")
    note.update({
    "title":"Remainder1",
    "public":1,
    "notify_on_login":1,
    "expire_notification_on":date,
    "content":content,   
    })
    note.save(ignore_permissions=True)
    frappe.db.commit()

