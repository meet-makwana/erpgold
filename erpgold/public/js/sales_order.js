frappe.ui.form.on('Sales Order Item', {
    
    custom_net_weight: function (frm, cdt, cdn){
        var child = locals[cdt][cdn];
        var net_weight=child.custom_net_weight;
        var purity_percent = child.custom_purity_percentage;
        var fine_weight= net_weight * (purity_percent / 100);
        var gold_rate = child.custom_gold_rate;
        var gold_value = (gold_rate / 10) * net_weight;

        frappe.model.set_value(cdt, cdn, 'custom_fine_weight', fine_weight);
        frappe.model.set_value(cdt, cdn, 'custom_gold_value', gold_value);
    },
    
    custom_discount: function (frm, cdt, cdn){
        var child = locals[cdt][cdn];
        var gold_value = child.custom_gold_value;
        var other_amount = child.custom_other_amount || 0;
        var labour_amount = child.custom_sales_labour_amount || 0;
        var discount = child.custom_discount || 0;
        var total_amount = (gold_value + other_amount + labour_amount) - discount;
        frappe.model.set_value(cdt, cdn, 'custom_total_amount', total_amount);
    },
    custom_labour_type: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var salesLabourAmount = 0;
        if (child.custom_labour_type === 'On Gross Weight Per Gram') {
            salesLabourAmount = child.qty * child.custom_sales_labour_rate * child.custom_gross_weight;
        } else if (child.custom_labour_type === 'On Net Weight Per Gram') {
            salesLabourAmount = child.qty * child.custom_sales_labour_rate * child.custom_net_weight;
        } else if (child.custom_labour_type === 'On Gold Value Percentage') {
            salesLabourAmount = child.qty * child.custom_sales_labour_rate * (child.custom_gold_value / 100);
        }
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', salesLabourAmount);
    },
    item_code: function (frm, cdt, cdn){
        var child = locals[cdt][cdn];
        var custom_purity = child.custom_purity;
        var mt = child.custom_metal_type;
        var date = frm.doc.transaction_date;
    
        frm.call({
            method: 'erpgold.erpgold.doctype.metal_rate.metal_rate.query',
            args: {
                date: date,
                metal_type: mt,
                purity: custom_purity
            },
            callback: function(r) {
                frappe.model.set_value(cdt, cdn, 'custom_gold_rate', r.message);
                refresh_field('custom_gold_rate');
            }
        });
    },
    custom_total_amount:function (frm, cdt, cdn){
        var child = locals[cdt][cdn];
        var rate = child.custom_total_amount;
        frappe.model.set_value(cdt, cdn, 'rate', rate);
    },
    
    custom_gross_weight:netweight,
    custom_less_weight:netweight,
});
function netweight(frm, cdt, cdn){
    var child = locals[cdt][cdn];
    var less_weight = child.custom_less_weight;
    var gross_weight = child.custom_gross_weight;
    var net_weight= gross_weight-less_weight;

    frappe.model.set_value(cdt, cdn, 'custom_net_weight', net_weight);
}

frappe.ui.form.on('Sales Order', {
    onload: function(frm) {
        frm.toggle_display(['timesheets','total_net_weight'], false);
        
        var today = frappe.datetime.get_today();

        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Metal Rate",
                filters: {
                    'date': today
                }
            },
            callback: function(r) {
                if (!(r.message && r.message.length > 0)) {
                    frappe.msgprint(__("Metal Rate for today has not been created. Please create Metal Rate first."));
                    frappe.validated = false;
                }
            }
        });
    }
});


