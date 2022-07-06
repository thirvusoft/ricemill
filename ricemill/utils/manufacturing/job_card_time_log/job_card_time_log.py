from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def job_card_time_log_customize_field():
    job_card_time_log_customize_field = {
        "Job Card Time Log": [
            dict(fieldname="shift_id",
                 label='Shift Id',
                 fieldtype='Int',
                 insert_after='completed_qty'
                 ),
            dict(fieldname="temperature",
                 label='Temperature',
                 fieldtype='Float',
                 insert_after='shift_id'
                 ),
            dict(fieldname="moisture",
                 label='Moisture',
                 fieldtype='Float',
                 insert_after='temperature'
                 ),
            dict(fieldname="machine_state",
                 label='Machine state',
                 fieldtype='Select',
                 options='\nheat\ncool\noff',
                 insert_after='temperature'
                 ),
        ]
    }

    create_custom_fields(job_card_time_log_customize_field)
