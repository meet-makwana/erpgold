# import frappe

# def custom_update_serial_nos_after_submit(controller, parentfield):
#     field = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
#              "custom_net_weight", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate", 
#              "custom_other_amount", "custom_sales_labour_type", "custom_sales_labour_amount", "custom_is_jewellery_item"]
    
#     # Fetch all Stock Ledger Entries associated with the voucher
#     sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=['serial_no', 'item_code'])
    
#     for s in sle:
#         # Check if the item has a serial number
#         if s['serial_no']:
#             # Fetch Serial No document for each serial number
#             target_doc = frappe.get_doc('Serial No', s['serial_no'])
            
#             if "Stock Entry" == controller.doctype:
#                 data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name, "item_code": s['item_code']}, fields=field)
#             elif "Purchase Receipt" == controller.doctype:
#                 data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name, "item_code": s['item_code']}, fields=field)
#             elif "Purchase Invoice" == controller.doctype:
#                 data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name, "item_code": s['item_code']}, fields=field)
#             else:
#                 frappe.msgprint("Not Available Serial No for this doctype")
#                 return
            
#             # Filter data based on item code and serial number
#             for record in data:
#                     target_doc.custom_size = record.get('custom_size')
#                     target_doc.custom_metal_type = record.get('custom_metal_type')
#                     target_doc.custom_purity = record.get('custom_purity')
#                     target_doc.custom_purity_percentage = record.get('custom_purity_percentage')
#                     target_doc.custom_gross_weight = record.get('custom_gross_weight')
#                     target_doc.custom_less_weight = record.get('custom_less_weight')
#                     target_doc.custom_net_weight = record.get('custom_net_weight')
#                     target_doc.custom_fine_weight = record.get('custom_fine_weight')
#                     target_doc.custom_gold_rate = record.get('custom_gold_rate')
#                     target_doc.custom_gold_value = record.get('custom_gold_value')
#                     target_doc.custom_mrp_rate = record.get('custom_mrp_rate')
#                     target_doc.custom_other_amount = record.get('custom_other_amount')
#                     target_doc.custom_labour_type = record.get('custom_sales_labour_type')
#                     target_doc.custom_sales_labour_rate = record.get('custom_sales_labour_rate')
#                     target_doc.custom_sales_labour_amount = record.get('custom_sales_labour_amount')
#                     target_doc.custom_is_jewellery_item = record.get('custom_is_jewellery_item')
#                     target_doc.save()
#         else:
#             frappe.msgprint("Serial Number not found for item {0}".format(s['item_code']))


# import frappe

# def custom_update_serial_nos_after_submit(controller, parentfield):
#     field = ["custom_size", "custom_metal_type", "custom_purity", "custom_purity_percentage", "custom_gross_weight", "custom_less_weight",
#              "custom_net_weight", "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate", "custom_value_added",
#              "custom_other_amount", "custom_sales_labour_type", "custom_sales_labour_amount", "custom_is_jewellery_item","image"]
    
#     # Fetch all Stock Ledger Entries associated with the voucher
#     sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=['serial_no', 'item_code'])
    
#     for s in sle:
        
#         # Check if the item has a serial number
#         if s['serial_no']:
#             # Fetch Serial No document for each serial number
#             target_doc = frappe.get_doc('Serial No', s['serial_no'])
            
#             if "Stock Entry" == controller.doctype:
#                 data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name, "item_code": s['item_code'], "serial_no": s['serial_no']}, fields=field)
#             elif "Purchase Receipt" == controller.doctype:
#                 data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name, "item_code": s['item_code'], "serial_no": s['serial_no']}, fields=field)
#             elif "Purchase Invoice" == controller.doctype:
#                 data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name, "item_code": s['item_code'], "serial_no": s['serial_no']}, fields=field)
#             else:
#                 frappe.msgprint("Not Available Serial No for this doctype")
#                 return
            
#             # Update Serial No document with fetched data
#             if data:
#                 record = data[0]
#                 target_doc.custom_item_image = record.get('image')
#                 target_doc.custom_size = record.get('custom_size')
#                 target_doc.custom_metal_type = record.get('custom_metal_type')
#                 target_doc.custom_purity = record.get('custom_purity')
#                 target_doc.custom_purity_percentage = record.get('custom_purity_percentage')
#                 target_doc.custom_gross_weight = record.get('custom_gross_weight')
#                 target_doc.custom_less_weight = record.get('custom_less_weight')
#                 target_doc.custom_net_weight = record.get('custom_net_weight')
#                 target_doc.custom_fine_weight = record.get('custom_fine_weight')
#                 target_doc.custom_gold_rate = record.get('custom_gold_rate')
#                 target_doc.custom_gold_value = record.get('custom_gold_value')
#                 target_doc.custom_mrp_rate = record.get('custom_mrp_rate')
#                 target_doc.custom_other_amount = record.get('custom_other_amount')
#                 target_doc.custom_labour_type = record.get('custom_sales_labour_type')
#                 target_doc.custom_sales_labour_rate = record.get('custom_value_added')
#                 target_doc.custom_sales_labour_amount = record.get('custom_sales_labour_amount')
#                 target_doc.custom_is_jewellery_item = record.get('custom_is_jewellery_item')
#                 target_doc.save()
#         else:
#             frappe.msgprint("Serial Number not found for item {0}".format(s['item_code']))

import frappe

@frappe.whitelist()
def custom_update_serial_nos_after_submit(controller, parentfield):
    field = ["custom_size", "image", "custom_metal_type", "custom_purity", "custom_purity_percentage", 
             "custom_gross_weight", "custom_less_weight", "custom_net_weight", "custom_westage", 
             "custom_fine_weight", "custom_gold_rate", "custom_gold_value", "custom_mrp_rate", 
             "custom_other_amount", "custom_sales_labour_type",# "custom_sales_labour_rate"*/, 
             "custom_sales_labour_amount", "custom_is_jewellery_item"]


    # #get all items from item table
    # itm = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype}, fields=['item_code'])
    # print("\n" +str(itm))
    # #for each item check if item has serial no
    # for item in itm:
    #     s=frappe.db.get_value("Item",filters={"item_code":item.item_code , "has_serial_no":'1'},fieldname="item_code")
    #     # print("\n" +str(s))
    #     #if has serial no no then proceed to generate serial no doc
    #     if(s):  
    #         #for each serialized item >>>>
    #         print("\n" +s)
    sle = frappe.db.get_all('Stock Ledger Entry', filters={"voucher_no": controller.name, "voucher_type": controller.doctype,}, fields=['serial_no', 'item_code', 'voucher_detail_no'])
    print("\n" +str(sle))
    for sle1 in sle: 
        vd = sle1['voucher_detail_no'].split('\n')
        for v in vd:
         if sle1['serial_no'] is not None:  # Check if serial_no is not None
            serial_numbers = sle1['serial_no'].split('\n')
            
            for serial_no in serial_numbers:
                if serial_no == '':
                    continue  # Skip empty serial numbers
                else:
                    serial_doc = frappe.get_doc('Serial No', serial_no)
                    if "Stock Entry" == controller.doctype:
                        data = frappe.db.get_all('Stock Entry Detail', filters={"parent": controller.name,"name":v , "item_code": sle1.item_code}, fields=field)
                    elif "Purchase Receipt" == controller.doctype:
                        data = frappe.db.get_all('Purchase Receipt Item', filters={"parent": controller.name, "name":v ,"item_code": sle1.item_code}, fields=field)
                    elif "Purchase Invoice" == controller.doctype:
                        data = frappe.db.get_all('Purchase Invoice Item', filters={"parent": controller.name,"name":v , "item_code": sle1.item_code}, fields=field)
                    else:
                        frappe.msgprint("Not Available Serial No for this doctype")
                        return

                    for record in data:
                        # Update Serial No document with data from voucher
                        serial_doc.custom_size = record.custom_size
                        serial_doc.custom_a_image = record.image
                        serial_doc.custom_metal_type = record.custom_metal_type
                        serial_doc.custom_purity = record.custom_purity
                        serial_doc.custom_purity_percentage = record.custom_purity_percentage
                        serial_doc.custom_gross_weight = record.custom_gross_weight
                        serial_doc.custom_less_weight = record.custom_less_weight
                        serial_doc.custom_net_weight = record.custom_net_weight
                        serial_doc.custom_westage = record.custom_westage
                        serial_doc.custom_fine_weight = record.custom_fine_weight
                        serial_doc.custom_gold_rate = record.custom_gold_rate
                        serial_doc.custom_gold_value = record.custom_gold_value
                        serial_doc.custom_mrp_rate = record.custom_mrp_rate
                        serial_doc.custom_other_amount = record.custom_other_amount
                        serial_doc.custom_labour_type = record.custom_sales_labour_type
                        serial_doc.custom_sales_labour_rate = record.custom_sales_labour_rate
                        serial_doc.custom_sales_labour_amount = record.custom_sales_labour_amount
                        serial_doc.custom_is_jewellery_item = record.custom_is_jewellery_item

                        # Save the changes to the serial number document
                        serial_doc.save()