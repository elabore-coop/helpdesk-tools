# Copyright 2024 Stéphan Sainléger ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "helpdesk_request_type",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Stéphan Sainléger",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Add request type field in helpdesk ticket.",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "helpdesk_mgmt",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/helpdesk_request_type.xml",
        "views/helpdesk_ticket.xml",
        "views/helpdesk_ticket_templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}