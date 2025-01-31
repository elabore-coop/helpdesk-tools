# Copyright 2024 Quentin Mondot
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk_create_task_from_ticket",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Quentin Mondot",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "This module enriches task information when creating it from a ticket form.",
    "depends": [
        "base",
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
        "helpdesk_request_type",  # to create the helpdesk.request.type model and have the field request_type_id in the helpdesk.ticket model
        "project_request_data"  # to have the fields service_id and request_type_id in the project.task model
    ],
    "data": [
        "views/helpdesk_create_task_from_ticket.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
