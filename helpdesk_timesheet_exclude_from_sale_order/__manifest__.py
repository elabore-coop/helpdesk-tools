# Copyright 2025 Boris Gallet (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk_timesheet_exclude_from_sale_order",
    "version": "16.0.1.0.0",
    "summary": "Exclude tickets from sale timesheets",
    "author": "Boris Gallet, Elabore Coop",
    "website": "https://elabore.coop",
    "license": "LGPL-3",
    "category": "Helpdesk",
    "depends": ["sale_timesheet_line_exclude","helpdesk_mgmt_timesheet"],
    "data": ["views/helpdesk_ticket.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
}