import frappe
from typing import Dict, Optional

BarcodeScanResult = Dict[str, Optional[str]]




@frappe.whitelist()
def custom_scan_barcode(search_value: str) -> BarcodeScanResult:
    def set_cache(data: BarcodeScanResult):
        frappe.cache().set_value(f"erpnext:barcode_scan:{search_value}", data, expires_in_sec=120)

    def get_cache() -> Optional[BarcodeScanResult]:
        if data := frappe.cache().get_value(f"erpnext:barcode_scan:{search_value}"):
            return data

    if scan_data := get_cache():
        return scan_data

    # search barcode no
    barcode_data = frappe.db.get_value(
        "Item Barcode",
        {"barcode": search_value},
        ["barcode", "parent as item_code","uom"],
        as_dict=True,
    )
    if barcode_data:
        _update_item_info(barcode_data)
        set_cache(barcode_data)
        return barcode_data

    # search serial no
    serial_no_data = frappe.db.get_value(
        "Serial No",
        search_value,
        ["name as serial_no", "item_code", "batch_no"],
        as_dict=True,
    )
    if serial_no_data:
        _update_item_info(serial_no_data)
        set_cache(serial_no_data)
        return serial_no_data

    # search batch no
    batch_no_data = frappe.db.get_value(
        "Batch",
        search_value,
        ["name as batch_no", "item as item_code"],
        as_dict=True,
    )
    if batch_no_data:
        _update_item_info(batch_no_data)
        set_cache(batch_no_data)
        return batch_no_data

    return {}


def _update_item_info(scan_result: Dict[str, Optional[str]]) -> Dict[str, Optional[str]]:
    if item_code := scan_result.get("item_code"):
        if item_info := frappe.get_cached_value(
            "Item",
            item_code,
            ["has_batch_no", "has_serial_no", "custom_metal_type","custom_purity","custom_purity_percentage_"],
            as_dict=True,
        ):
            scan_result.update(item_info)
            print(item_info)
            print(scan_result)
    return scan_result