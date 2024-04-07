# Copyright (c) 2024, Meet Makwana and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class MetalRate(Document):
	@frappe.whitelist()
	def get_metal_list(self):
		metal_list = frappe.get_all("Purity", fields=["metal_type","purity"])
		return metal_list

@frappe.whitelist()
def query(metal_type, purity, date):
    return frappe.db.sql("""
						 SELECT metal_rate
						 FROM `tabDaily Metal Rate` AS dmr
						 INNER JOIN `tabMetal Rate` AS mr
						 ON dmr.parent = mr.name
						 WHERE mr.docstatus = '1' AND metal_type = %s AND purity = %s AND mr.date = %s
						 """, (metal_type, purity, date))