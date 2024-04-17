
from erpnext.accounts.utils import get_fiscal_year
from frappe.model.document import Document
import frappe

class GoldLedger(Document):
    pass

@frappe.whitelist()
def on_submit(doc, method):
    fiscal_year = get_fiscal_year(doc.posting_date, company="ERPGold")[0]
    
    # if doc.doctype == "Delivery Note":
    #     items = frappe.get_all("Delivery Note Item", filters={"parent": doc.name}, fields=["item_code","custom_purity","serial_no","custom_purity_percentage","custom_fine_weight","warehouse","amount"])
        
    # elif doc.doctype == "Purchase Receipt":
    #     items = frappe.get_all("Purchase Receipt Item", filters={"parent": doc.name}, fields=["item_code","custom_purity","serial_no","custom_purity_percentage","custom_fine_weight","warehouse","amount"])

    # elif doc.doctype=="Stock Entry":
    #     items=frappe.get_all("Stock Entry Item",filters={"parent": doc.name}, fields=["item_code","custom_purity","serial_no","custom_purity_percentage","custom_fine_weight","warehouse","amount"])  

    # elif doc.doctype=="Purchase Invoice":
    #     items=frappe.get_all("Purchase Invoice Item",filters={"parent": doc.name}, fields=["item_code","custom_purity","serial_no","custom_purity_percentage","custom_fine_weight","warehouse","amount"])  

    # else:
    #     frappe.throw("Unsupported document type")

    for item in doc.items:
        if item.serial_no:
            gold_ledger_entry = frappe.new_doc("Gold Ledger")
            gold_ledger_entry.posting_date = doc.posting_date
            gold_ledger_entry.item_code = item.item_code
            gold_ledger_entry.purity = item.custom_purity
            gold_ledger_entry.purity_percentage = item.custom_purity_percentage
            gold_ledger_entry.serial_no = item.serial_no
            gold_ledger_entry.warehouse = item.warehouse
          
            if doc.doctype == "Delivery Note" :
                gold_ledger_entry.debit_gold = item.custom_fine_weight
                gold_ledger_entry.debit_in_account_currency = item.amount
                gold_ledger_entry.debit = item.amount
                gold_ledger_entry.party = doc.customer
                gold_ledger_entry.party_type = "customer"
            elif doc.doctype == "Purchase Receipt" or doc.doctype == "Purchase Invoice" or doc.doctype == "Stock Entry":
                gold_ledger_entry.credit_gold = item.custom_fine_weight
                gold_ledger_entry.credit_in_account_currency = item.amount
                gold_ledger_entry.credit = item.amount
                gold_ledger_entry.party =doc.supplier
                gold_ledger_entry.party_type ="Supplier"
            gold_ledger_entry.account_currency = doc.currency
            gold_ledger_entry.voucher_type = doc.doctype
            gold_ledger_entry.voucher_no = doc.name
            gold_ledger_entry.fiscal_year = fiscal_year
            
            gold_ledger_entry.insert()
            frappe.msgprint('Added Gold Ledger Entry  ', indicator='green', alert=True)

@frappe.whitelist()
def cancel(doc, method):
       frappe.db.set_value("Gold Ledger", {"voucher_type": doc.doctype, "voucher_no": doc.name}, "is_cancelled", 1)
       frappe.msgprint('Gold Ledger Entry Cancelled', indicator='red', alert=True)
#    pass 

