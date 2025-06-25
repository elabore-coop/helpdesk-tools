# Copyright 2024 Quentin Mondot
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk_convert_ticket_to_task",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Quentin Mondot",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "This module adds a button to convert a ticket into a task.",
    "depends": [
        "base",
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
        # to create the helpdesk.request.type model and have the field request_type_id
        # in the helpdesk.ticket model
        "helpdesk_request_type",
        # to have the fields service_id and request_type_id in the project.task model
        "project_request_data",
        "project_task_add_very_high",  # to have priority values 2 and 3 on tasks
        "helpdesk_transfer_timesheet_to_task",  # to copy timesheets from ticket to task
    ],
    "data": [
        "views/helpdesk_convert_ticket_to_task.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
