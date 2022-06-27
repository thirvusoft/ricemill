from ricemill.utils.accounts.sales_invoice import customize_field
from ricemill.utils.manufacturing.workstation.workstation_working_hour import workstation_customize_field
from ricemill.utils.manufacturing.operation.operation import operation_customize_field
from ricemill.utils.stock.item.custom_fields_item import item_field_customize
from ricemill.utils.stock.item.custom_fields_item import property_setter_item_field
from ricemill.utils.desk.note.note import remainder_note
from ricemill.utils.manufacturing.bom.bom import bom_customize_field
from ricemill.utils.accounts.sales_invoice import customize_field
from ricemill.utils.manufacturing.workstation.workstation_working_hour import workstation_customize_field
from ricemill.utils.manufacturing.operation.operation import operation_customize_field
from ricemill.utils.manufacturing.work_order.work_order import work_order_customize_field
from ricemill.utils.manufacturing.job_card.jobcard import job_card_customize_field
def after_install():
    customize_field()
    workstation_customize_field()
    operation_customize_field()
    item_field_customize()
    property_setter_item_field()
    remainder_note()
    bom_customize_field()
    work_order_customize_field()
    job_card_customize_field()

