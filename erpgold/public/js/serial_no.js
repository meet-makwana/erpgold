// frappe.ui.form.on('Serial No',{
//     setup:function(frm,cdt,cdn){
//         frm.call({        
//             method: 'erpgold.erpgold.doctype.stock_audit.stock_audit.fetchvalue',
//             args:{           
//                 doc_no:frm.doc.purchase_document_no,            
//             },
//             callback: function(r) {
                
//                 var data = r.message[0];
//                 frm.set_value("custom_metal_type",data.custom_metal_type);
//                 frm.set_value("custom_size",data.custom_size);
//                 frm.set_value("custom_purity",data.custom_purity);
//                 frm.set_value("custom_purity_percentage",data.custom_purity_percentage);
//                 frm.set_value("custom_gross_weight",data.custom_gross_weight);
//                 frm.set_value("custom_less_weight",data.custom_less_weight);
//                 frm.set_value("custom_net_weight",data.custom_net_weight);
//                 frm.set_value("custom_westage",data.custom_westage);
//                 frm.set_value("custom_fine_weight",data.custom_fine_weight);
//                 frm.set_value("custom_gold_rate",data.custom_gold_rate);
//                 frm.set_value("custom_gold_value",data.custom_gold_value);
//                 frm.set_value("custom_mrp_rate",data.custom_mrp_rate);
//                 frm.set_value("custom_other_amount",data.custom_other_amount);
//                 frm.set_value("custom_labour_type",data.custom_sales_labour_type);
//                 frm.set_value("custom_sales_labour_rate",data.custom_value_added);
//                 frm.set_value("custom_sales_labour_amount",data.custom_sales_labour_amount);
//                 frm.set_value("custom_is_jewellery_item",data.custom_is_jewellery_item);
//                 frm.save();     
    
//             }
            
//         });





//     }
// })