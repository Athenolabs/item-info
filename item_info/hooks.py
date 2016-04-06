# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "item_info"
app_title = "Item Info"
app_publisher = "Frappe"
app_description = "Items Details"
app_icon = "icon-truck"
app_color = "blue"
app_email = "jitendra.k@indictranstech.com"
app_version = "0.0.1"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/item_info/css/item_info.css"
# app_include_js = "/assets/item_info/js/item_info.js"

# include js, css files in header of web template
# web_include_css = "/assets/item_info/css/item_info.css"
# web_include_js = "/assets/item_info/js/item_info.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "item_info.utils.get_home_page"
# Add Fixtures
fixtures =['Custom Field', "Property Setter","Custom Script"]
# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "item_info.install.before_install"
# after_install = "item_info.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "item_info.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"item_info.tasks.all"
# 	],
# 	"daily": [
# 		"item_info.tasks.daily"
# 	],
# 	"hourly": [
# 		"item_info.tasks.hourly"
# 	],
# 	"weekly": [
# 		"item_info.tasks.weekly"
# 	]
# 	"monthly": [
# 		"item_info.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "item_info.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "item_info.event.get_events"
# }

