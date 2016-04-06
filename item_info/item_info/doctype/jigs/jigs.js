// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt
frappe.ui.form.on("Jig Item",{
	item:function(frm,cdt,cdn){
		var d = locals[cdt][cdn];
		if(d.item){
			frappe.call({
		        method: "item_info.item_info.doctype.jigs.jigs.get_actual_qty",
		        args: {
		            "item_code": d.item
		        },
		       	callback: function(r){
			       	if(r.message){
			       		d.qty = r.message
			       		refresh_field("jig_item")
		       		}
		       		else{
		       			d.qty = ""
			       		refresh_field("jig_item")	
		       		}
		       	}
			})
		}
	},
});