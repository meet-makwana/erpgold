app_name = "erpgold"
app_title = "ERPGold"
app_publisher = "Meet Makwana"
app_description = "ERP Gold is a comprehensive and cutting-edge enterprise resource planning (ERP) software designed to streamline and optimize business operations across various departments. With its powerful features and intuitive interface, ERP Gold empowers organizations to enhance productivity, reduce costs, and make informed strategic decisions."
app_email = "makwanameet20@gmail.com"
app_license = "MIT"




fixtures = [
    {
    "dt": ("Custom Field"), 
        "filters": [["dt", "in", ("Item","Sales Invoice","Sales Invoice Item","Sales Order","Sales Order Item","Sales Order","Sales Order Item","Delivery Note","Delivery Note Item","Purchase Invoice","Purchase Invoice Item","Purchase Receipts","Purchase Rececipts Item","Purchase Order","Purchase Order Item","Stock Entry","Stock Entry Detail","Serial No","Payment Entry","Customer")]]
    }
    
]
app_include_js=[
    "/assets/erpgold/js/barcode_scan.js"
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpgold/css/erpgold.css"
# app_include_js = "/assets/erpgold/js/erpgold.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpgold/css/erpgold.css"
# web_include_js = "/assets/erpgold/js/erpgold.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpgold/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : ["public/js/sales_invoice_item.js"],"Sales Order" : ["public/js/sales_order.js"],"Delivery Note" : ["public/js/delivery_note.js"],"Purchase Invoice" : ["public/js/purchase_invoice.js"],"Purchase Receipt" : ["public/js/purchase_receipt.js"],"Purchase Order" : ["public/js/purchase_order.js"],"Stock Entry" : ["public/js/stock_entry.js"],"Serial No" : ["public/js/serial_no.js"]}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "erpgold.utils.jinja_methods",
# 	"filters": "erpgold.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpgold.install.before_install"
# after_install = "erpgold.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpgold.uninstall.before_uninstall"
# after_uninstall = "erpgold.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "erpgold.utils.before_app_install"
# after_app_install = "erpgold.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "erpgold.utils.before_app_uninstall"
# after_app_uninstall = "erpgold.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpgold.notifications.get_notification_config"

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
# 	"PurchaseReceipt": "erpgold.serial_no_data.serial_no_data"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Purchase Receipt": {
		"on_submit": "erpgold.serial_no_data.on_submit"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpgold.tasks.all"
# 	],
# 	"daily": [
# 		"erpgold.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpgold.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpgold.tasks.weekly"
# 	],
# 	"monthly": [
# 		"erpgold.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "erpgold.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpgold.event.get_events"
# }
# override_update_serial_nos_after_submit_method={
#     "erpnext.update_serial_nos_after_submit_method"="erpgold.barcode.generate_serial_no"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpgold.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# --------------------------------------------------------------------- 

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erpgold.utils.before_request"]
# after_request = ["erpgold.utils.after_request"]

# Job Events
# ----------
# before_job = ["erpgold.utils.before_job"]
# after_job = ["erpgold.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erpgold.auth.validate"
# ]
