from ricemill.utils.stock.item.quality_inspection import quality_inspection_customize_field
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
from ricemill.utils.manufacturing.work_order.work_order import customize_work_order
from ricemill.utils.manufacturing.job_card.jobcard import customize
from ricemill.utils.manufacturing.job_card_time_log.job_card_time_log import job_card_time_log_customize_field
from ricemill.custom.warehouse import create_fields
from ricemill.utils.stock.item.quality_inspection import quality_inspection_fields
from ricemill.utils.manufacturing.work_order.work_order import work_order_customize_field
from ricemill.utils.manufacturing.job_card.jobcard import job_card_customize_field
from ricemill.utils.stock.stock_entry.stock_entry import create_stock_entry_custom_field()
def after_install():
    customize_field()
    workstation_customize_field()
    operation_customize_field()
    item_field_customize()
    property_setter_item_field()
    remainder_note()
    bom_customize_field()
    quality_inspection_customize_field()
    customize_work_order()
    customize()
    job_card_time_log_customize_field()
    create_fields()
    quality_inspection_fields()
    work_order_customize_field()
    job_card_customize_field()
    create_stock_entry_custom_field()
