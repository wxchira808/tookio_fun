app_name = "tookio_fun"
app_title = "Tookio Fun"
app_publisher = "Brian Wachira"
app_description = "A fun collection of vibe coded projects."
app_email = "bwkinyua01@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tookio_fun",
# 		"logo": "/assets/tookio_fun/logo.png",
# 		"title": "Tookio Fun",
# 		"route": "/tookio_fun",
# 		"has_permission": "tookio_fun.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tookio_fun/css/tookio_fun.css"
# app_include_js = "/assets/tookio_fun/js/tookio_fun.js"

# include js, css files in header of web template
# web_include_css = "/assets/tookio_fun/css/tookio_fun.css"
# web_include_js = "/assets/tookio_fun/js/tookio_fun.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tookio_fun/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tookio_fun/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tookio_fun.utils.jinja_methods",
# 	"filters": "tookio_fun.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tookio_fun.install.before_install"
# after_install = "tookio_fun.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tookio_fun.uninstall.before_uninstall"
# after_uninstall = "tookio_fun.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tookio_fun.utils.before_app_install"
# after_app_install = "tookio_fun.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tookio_fun.utils.before_app_uninstall"
# after_app_uninstall = "tookio_fun.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tookio_fun.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tookio_fun.tasks.all"
# 	],
# 	"daily": [
# 		"tookio_fun.tasks.daily"
# 	],
# 	"hourly": [
# 		"tookio_fun.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tookio_fun.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tookio_fun.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tookio_fun.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tookio_fun.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tookio_fun.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tookio_fun.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tookio_fun.utils.before_request"]
# after_request = ["tookio_fun.utils.after_request"]

# Job Events
# ----------
# before_job = ["tookio_fun.utils.before_job"]
# after_job = ["tookio_fun.utils.after_job"]

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
# 	"tookio_fun.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

