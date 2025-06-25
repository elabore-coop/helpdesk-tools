# Copyright 2024 Quentin Mondot
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk_transfer_timesheet_to_task",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://github.com/elabore-coop/helpdesk-tools",
    "maintainer": "Quentin Mondot",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "This module assigns timesheets to the task linked to a ticket.",
    "depends": [
        "base",
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
        "helpdesk_mgmt_timesheet",
        "sale_timesheet",
    ],
    "data": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}
