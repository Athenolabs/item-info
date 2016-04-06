frappe.ui.form.on("Quotation","refresh", function(frm) {
        cur_frm.fields_dict.items.grid.get_field("item_code").get_query = function(doc) {
        var t_list = []
        for(var i = 0 ; i < cur_frm.doc.items.length ; i++){
            if(cur_frm.doc.items[i].item_code){
                t_list.push(cur_frm.doc.items[i].item_code);
            }
        }
        return {
            filters: [
                ['Item', 'name', 'not in', t_list]
            ]
        }   
    }
});


frappe.ui.form.on("Quotation Item", {
    relative_items: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn]
        var me = this;            
        this.dialog = new frappe.ui.Dialog({
            title: "Select Relative Items",
                fields: [
                   {"fieldtype": "HTML" , "fieldname": "relative_items" , "label": "Relative Items"},
                   ],
                   primary_action_label: "Add",
                    primary_action: function(){
                        add_quotation_items(me.dialog)
                    }
            });
        fd = this.dialog.fields_dict;
        frappe.call({
            method: "item_info.item_info.doctype.jigs.jigs.get_relative_items",
            args: {
                "item_code":d.item_code,
                "item_name":d.item_name
            },
            callback: function(r){
                var related_list = []
                if(cur_frm.doc.related_items){
                    for(var i = 0 ; i < cur_frm.doc.related_items.length ; i++){
                        if(cur_frm.doc.related_items[i].item_code){
                            related_list.push(cur_frm.doc.related_items[i].item_code);
                        }
                    }
                }
                if(r.message){
                    r.message["Suggested Items"] = filter(r.message["Suggested Items"],related_list)
                    r.message["Alternate Items"] = filter(r.message["Alternate Items"],related_list)
                    r.message["Accessory Items"] = filter(r.message["Accessory Items"],related_list)
                    var Suggested = r.message["Suggested Items"]
                    var alternative = r.message["Alternate Items"]
                    var accessories = r.message["Accessory Items"]
                    max = Math.max(Suggested.length,alternative.length,accessories.length);
                    if(max > 0){
                        $(frappe.render_template("relative_items",{"items":r.message,"max":max})).appendTo(me.dialog.fields_dict.relative_items.$wrapper);
                        me.dialog.show();
                        /*$('.member').click(function (){
                            var checkbox = $(this).find('input[type=checkbox]');
                            checkbox.prop("checked", !checkbox.prop("checked"));
                        });*/
                    }
                    else{
                        msgprint("All Related Items For Item Code - " +" "+ d.item_code +"\n"+"Already Added To Related Items Table")
                    }
                }
                else{
                    msgprint("No Related Items For Item Code - " +" "+ d.item_code)    
                }
            }
        });
        add_quotation_items =function(){
            var items_to_add = []
            $.each($(fd.relative_items.wrapper).find(".select:checked"), function(value, item){
                items_to_add.push($(item).val());
            });
            if(items_to_add.length > 0){
                frappe.call({
                    method:"item_info.item_info.doctype.jigs.jigs.items_details",
                    args: { 
                        "item_list": items_to_add,
                        "item_code":d.item_code
                    },
                    callback: function(r) {
                        $.each(r.message, function(i, d) {
                            var row = frappe.model.add_child(cur_frm.doc, "Related Item", "related_items");
                            row.item_code = d.item_code;
                            row.item_name = d.item_name;
                            row.item_type = d.item_type;
                            row.parent_item = d.name;
                            row.rate = 0;
                        })
                        refresh_field("related_items");
                        dialog.hide()
                    }
                });
            }
            else{
                msgprint("Select Item Before Add")
            }
        }    
    },
});

filter = function(arr1, arr2) {      //filter related item template
    return arr1.filter(function(obj) {
    return !inList(arr2,obj.item_code)
    });
};