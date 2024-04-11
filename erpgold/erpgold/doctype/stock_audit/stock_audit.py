# custom_app/custom_module/custom_script.py
import frappe
from frappe.model.document import Document

class StockAudit(Document):
    
   
    @frappe.whitelist()
    def get_serial_numbers(self):
        self.total_items_in_stock = frappe.db.count('Serial No', {'status': 'Active'})
        serial_numbers = frappe.get_all('Serial No', filters={'status': 'Active'}, fields=['name', 'item_code'])
        return serial_numbers
    
    @frappe.whitelist()
    def get_serial_numbers_2(self, scanned_serial_no):
        serial_number = frappe.get_all('Serial No', filters={ 'name': scanned_serial_no}, fields=['name', 'item_code','status'])
        if serial_number:
            return serial_number
        else:
           frappe.msgprint('Cannot find item with this barcode', indicator='red', alert=True)
           return False
        
    def validate(self):
        # Check if all items in the stock item table have been checked
        all_checked = all(row.item_checked == 1 for row in self.get('stock_item'))
        if not all_checked:
            frappe.throw('Please check all items before submitting.', title='Error')
