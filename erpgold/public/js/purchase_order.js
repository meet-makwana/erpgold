frappe.ui.form.on('Purchase Order Item', {
    
    
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
    
    custom_other_amount: function (frm, cdt, cdn){
        var child = locals[cdt][cdn];
        var gold_value = child.custom_gold_value;
        var other_amount = child.custom_other_amount || 0;
        var labour_amount = child.custom_sales_labour_amount || 0;
        var discount = child.custom_discount || 0;
        var total_amount = (gold_value + other_amount + labour_amount) - discount;
        frappe.model.set_value(cdt, cdn, 'custom_total_amount', total_amount);
    },
    custom_sales_labour_type: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var salesLabourAmount = 0;
        if (child.custom_sales_labour_type === 'On Gross Weight Per Gram') {
            salesLabourAmount = child.qty * child.custom_value_added * child.custom_gross_weight;
        } else if (child.custom_sales_labour_type === 'On Net Weight Per Gram') {
            salesLabourAmount = child.qty * child.custom_value_added * child.custom_net_weight;
        } else if (child.custom_sales_labour_type === 'On Gold Value Percentage') {
            salesLabourAmount = child.qty * child.custom_value_added * (child.custom_gold_value / 100);
        }
        frappe.model.set_value(cdt, cdn, 'custom_sales_labour_amount', salesLabourAmount);
    },
    custom_labour_type: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var LabourAmount = 0;
        if (child.custom_labour_type === 'On Gross Weight Per Gram') {
            LabourAmount = child.qty * child.custom_labour_rate * child.custom_gross_weight;
        } else if (child.custom_labour_type === 'On Net Weight Per Gram') {
            LabourAmount = child.qty * child.custom_labour_rate * child.custom_net_weight;
        } else if (child.custom_labour_type === 'On Gold Value Percentage') {
            LabourAmount = child.qty * child.custom_labour_rate * (child.custom_gold_value / 100);
        }
        frappe.model.set_value(cdt, cdn, 'custom_labour_amount', LabourAmount);
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
    custom_fine_weight:function (frm){
        var total_net_weight = 0;
        var total_fine_weight=0;
        var total_gross_weight =0;
        var total_less_weight=0;
    
        frm.doc.items.forEach(function(item) {
            total_net_weight =total_net_weight+ (item.custom_net_weight*item.qty)||0;
        });
        frm.set_value('custom_total_net_weight', total_net_weight);
    
        frm.doc.items.forEach(function(item) {
            total_fine_weight =total_fine_weight+ (item.custom_fine_weight*item.qty)||0;
        });
        frm.set_value('custom_total_fine_weight', total_fine_weight);
    
        frm.doc.items.forEach(function(item) {
            total_gross_weight =total_gross_weight+ (item.custom_gross_weight*item.qty)||0;
        });
        frm.set_value('custom_total_gross_weight', total_gross_weight);
    
        frm.doc.items.forEach(function(item) {
            total_less_weight =total_less_weight+ (item.custom_less_weight*item.qty)||0;
        });
        frm.set_value('custom_total_less_weight', total_less_weight);
    },
    custom_gross_weight:netweight,
    custom_less_weight:netweight,
    custom_fine_weight:calculateFineValue,
    custom_booking_rate:calculateFineValue
    
});
function netweight(frm, cdt, cdn){
    var child = locals[cdt][cdn];
    var less_weight = child.custom_less_weight;
    var gross_weight = child.custom_gross_weight;
    var net_weight= gross_weight-less_weight;

    frappe.model.set_value(cdt, cdn, 'custom_net_weight', net_weight);
};
function calculateFineValue(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var fine_weight = child.custom_fine_weight;
    var booking_rate = frm.doc.custom_booking_rate;
    var fine_value = fine_weight * booking_rate;
    
        
    frappe.model.set_value(cdt, cdn, 'custom_fine_value', fine_value);
}



frappe.ui.form.on('Purchase Invoice', {
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
    },
    
}
);
    
    
