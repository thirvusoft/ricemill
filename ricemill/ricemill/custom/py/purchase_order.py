import frappe


def username_validate(doc, action):
    user = frappe.session.user
    if(user != 'Administrator'):
        username = frappe.get_all(
            "User", filters={'email': user}, pluck='username')[0]
        doc.user_name = username
    else:
        doc.user_name = "Administrator"
