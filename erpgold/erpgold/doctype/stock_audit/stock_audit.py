# Copyright (c) 2024, Meet Makwana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StockAudit(Document):
     pass



# @frappe.whitelist()
# def fetchvalue(doc_no):
#         stock_entry = frappe.db.get_all("Stock Entry Detail", filters={"parent": doc_no}, fields=["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_fine_weight","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_sales_labour_type","custom_value_added","custom_sales_labour_amount","custom_is_jewellery_item"])
#         if stock_entry:
#             return stock_entry
        
#         purchase_receipt = frappe.db.get_all("Purchase Receipt Item", filters={"parent": doc_no}, fields=["custom_size","custom_metal_type","custom_purity","custom_purity_percentage","custom_gross_weight","custom_less_weight","custom_net_weight","custom_fine_weight","custom_westage","custom_gold_rate","custom_gold_value","custom_mrp_rate","custom_other_amount","custom_sales_labour_type","custom_value_added","custom_sales_labour_amount","custom_is_jewellery_item"])
#         if purchase_receipt:
#             return purchase_receipt
