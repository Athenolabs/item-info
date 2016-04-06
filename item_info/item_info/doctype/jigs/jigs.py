# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class Jigs(Document):
	pass

@frappe.whitelist()
def get_actual_qty(item_code):
	actual_qty = frappe.db.get_value("Bin",{"item_code":item_code},"sum(actual_qty)")
	return actual_qty

@frappe.whitelist()
def get_relative_items(item_code,item_name):
	relative_items = {
					"Suggested Items":common_query(item_code,item_name,"Suggested Items"),
					"Alternate Items":common_query(item_code,item_name,"Alternate Items"),
					"Accessory Items":common_query(item_code,item_name,"Accessory Items")
					}
	if len(relative_items["Suggested Items"]) > 0 or len(relative_items["Alternate Items"]) > 0 or len(relative_items["Accessory Items"]) > 0:				
		return relative_items	

def common_query(item_code,item_name,type):
	return frappe.db.sql("""select t1.item_code 
							from `tabItemType`t1,`tabItem`t2 
							where t1.parent = t2.name 
							and t1.item_type = '{0}' 
							and t2.name = '{1}' 
							and t2.item_code = '{2}' """.format(type,item_name,item_code),as_dict=1)	
	
@frappe.whitelist()
def items_details(item_list,item_code):
	current_list = json.loads(item_list)
	list2 = tuple([x.encode('UTF8') for x in list(current_list) if x])
	if len(current_list) == 1:
		cond = "t1.item_code =  {0} ".format(item_list[1:len(item_list) - 1])
	elif len(current_list) > 1:
		cond = "t1.item_code in {0}".format(list2)
	
	items_details = frappe.db.sql("""select t1.item_code,t1.item_name,t1.item_type,t2.name 
									from `tabItemType`t1,
									`tabItem`t2
									where {0} 
									and t1.parent = t2.name
									and t2.name = '{1}' """.format(cond,item_code),as_dict=1)
	return items_details
