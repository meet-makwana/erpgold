frappe.ui.form.on('Stock Audit', {
    onload: function(frm) {
        // Fetch serial numbers
        frappe.call({
            doc: frm.doc,
            method: 'get_serial_numbers',
            callback: function(response) {
                if (response.message) {
                    response.message.forEach(function(serial) {
                        var row = frappe.model.add_child(frm.doc, 'Stock Item', 'stock_item');
                        row.serial_no = serial.name;
                        row.item_code = serial.item_code;
                    });
                    frm.refresh_field('stock_item');
                    frm.refresh_field('total_items_in_stock');
                }
            }
        });
    },
    scan_barcode: function(frm) {
        if (frm.doc.scan_barcode != '') {
            var scanned_serial_no = frm.doc.scan_barcode;

            // Check if the scanned serial number already exists in not_in_stock
            var serial_exists = frm.doc.not_in_stock.some(function(row) {
                return row.serial_no === scanned_serial_no;
            });

            if (serial_exists) {
                frappe.show_alert({
                    message:__('Item already checked'),
                    indicator:'green'
                });
                frm.set_value('scan_barcode', '');
                return;
            }

            // Check if the scanned serial number is already in stock_item
            var found_in_stock = false;
            frm.doc.stock_item.forEach(function(row) {
                if (row.serial_no === scanned_serial_no) {
                    if (row.item_checked == 1) {
                        frappe.show_alert({
                            message:__('Item already checked'),
                            indicator:'green'
                        });
                    } else {
                        row.item_checked = 1;
                        frm.refresh_field('stock_item');
                        frappe.show_alert({
                            message:__('Item checked'),
                            indicator:'green'
                        });
                    }
                    found_in_stock = true;
                    return false;
                }
            });

            if (!found_in_stock) {
                // Call get_serial_numbers_2 to check the status of the scanned serial number
                frappe.call({
                    doc: frm.doc,
                    method: 'get_serial_numbers_2',
                    args: {
                        scanned_serial_no: scanned_serial_no
                    },
                    callback: function(response) {
                        if (response.message) {
                            response.message.forEach(function(serial) {
                                if (serial.status === 'Delivered') {
                                    // If status is 'Delivered', add to not_in_stock
                                    var row = frappe.model.add_child(frm.doc, 'Not in Stock', 'not_in_stock');
                                    frappe.model.set_value(row.doctype, row.name, 'serial_no', serial.name);
                                    frappe.model.set_value(row.doctype, row.name, 'item_code', serial.item_code);
                                    frm.refresh_field('not_in_stock');
                                    frappe.show_alert({
                                        message:__('Item added to Not in Stock'),
                                        indicator:'green'
                                        
                                    });
                                    
                                } else if (serial.status === 'Inactive') {
                                    // If status is 'Inactive', increment total_not_found_items
                                    frm.set_value('total_not_found_items', frm.doc.total_not_found_items + 1);
                                    frappe.show_alert({
                                        message:__('Item Not Found'),
                                        indicator:'red'
                                        
                                    });
                                }
                            });
                            var total_count = frm.doc.not_in_stock.reduce(function(acc, row) {
                                return acc + 1;
                            }, 0);
                                
                            frm.set_value('total_not_in_stock_items', total_count);
                            frm.refresh_field('not_in_stock');
                        } 
                        frm.set_value('scan_barcode', '');
                    }
                });
            }
            frm.set_value('scan_barcode','');
        }
    }
});
