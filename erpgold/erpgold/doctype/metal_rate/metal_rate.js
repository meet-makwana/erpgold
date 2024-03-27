// Copyright (c) 2024, Meet Makwana and contributors
// For license information, please see license.txt
frappe.ui.form.on('Metal Rate', {


    get_metal_list: function (frm) {
        frappe.call({
			doc : frm.doc,
            method: 'get_metal_list',
            args: {
            },
            callback: function (r) {
                if (r.message) {
                    frm.clear_table("daily_metal_rate");
                    $.each(r.message, function (index, data) {
                        var child = frm.add_child("daily_metal_rate");
                        frappe.model.set_value(child.doctype, child.name, "metal_type", data.metal_type);
                        frappe.model.set_value(child.doctype, child.name, "purity", data.purity);
                        frappe.model.set_value(child.doctype, child.name, "rate", data.rate);
                    });
                    frm.refresh_field("daily_metal_rate");
                }
            }
        });
    }
}); 


