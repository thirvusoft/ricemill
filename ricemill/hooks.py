from . import __version__ as app_version

app_name = "ricemill"
app_title = "Ricemill"
app_publisher = "Thirvusoft"
app_description = "rice mill"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "thirvusoft@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ricemill/css/ricemill.css"
# app_include_js = "/assets/ricemill/js/ricemill.js"

# include js, css files in header of web template
# web_include_css = "/assets/ricemill/css/ricemill.css"
# web_include_js = "/assets/ricemill/js/ricemill.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ricemill/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {

    "Work Order": "ricemill/custom/js/workorder.js",
    "Job Card": "ricemill/custom/js/job_card.js",
    "Operation": "ricemill/custom/js/operation.js",
    "Purchase Order": "ricemill/custom/js/purchase_order.js",
    "Purchase Receipt": "ricemill/custom/js/purchase_receipt.js",
    "Purchase Invoice": "ricemill/custom/js/purchase_invoice.js",
    "Warehouse": "ricemill/custom/js/warehouse.js"
}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ricemill.install.before_install"

after_install = "ricemill.utils.after_install.after_install"

# Uninstallation

# before_uninstall = "ricemill.uninstall.before_uninstall"
# after_uninstall = "ricemill.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ricemill.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {


    "Sales Invoice": {
        "validate": "ricemill.ricemill.custom.js.python.sales_invoice.calc_commission",
        "on_submit": "ricemill.ricemill.custom.js.python.sales_invoice.create_gl_entry",
        # "on_trash": "method"
    },
    "Job Card": {
        "before_submit": "ricemill.ricemill.custom.py.job_card.before_submit"
    },
    "Work Order": {
        "before_submit": "ricemill.ricemill.custom.py.workorder.before_submit"
    },
    "BOM": {
        'validate': "ricemill.ricemill.custom.py.bom.validate"
    },
    "Purchase Order": {
        'validate': "ricemill.ricemill.custom.py.purchase_order.username_validate"
    },
    "Stock Ledger Entry": {
        "before_submit": "ricemill.ricemill.custom.py.stock_ledger_entry.validate_warehouse",
        "on_submit": "ricemill.ricemill.custom.py.stock_ledger_entry.create_stock_entry"
    },
    "Purchase Receipt": {
        "before_submit": "ricemill.ricemill.custom.py.stock_ledger_entry.validate_warehouse"
    },
    "Purchase Invoice": {
        "before_submit": "ricemill.ricemill.custom.py.stock_ledger_entry.validate_warehouse"
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    # "all": [
    # 	"ricemill.custom.note.remainder_note"
    # ],
    "daily": [
        "ricemill.utils.desk.note.note.remainder_note"
    ],
    # "hourly": [
    # 	"ricemill.custom.note.remainder_note"
    # ],
    # "weekly": [
    # 	"ricemill.tasks.weekly"
    # ]
    # "monthly": [
    # 	"ricemill.tasks.monthly"
    # ]
}

# Testing
# -------

# before_tests = "ricemill.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ricemill.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ricemill.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {
        "doctype": "{doctype_4}"
    }
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ricemill.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
