from dataclasses import fields
import frappe
def stock_level(self,level):
    all_item=frappe.db.get_all("Bin",pluck="actual_qty" ,filters={"item_code":self.item_code})
    tot_stock=sum(all_item)
    self.stock_level=tot_stock
    print("---------------------------------------------------------------------------------------------------------------------------------")