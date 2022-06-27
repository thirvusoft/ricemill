from  ricemill.utils.stock.item.custom_fields_item import item_field_customize
from  ricemill.utils.stock.item.custom_fields_item import property_setter_item_field
from  ricemill.utils.desk.note.note import remainder_note 

def after_install():
    item_field_customize()
    property_setter_item_field()
    remainder_note()
    