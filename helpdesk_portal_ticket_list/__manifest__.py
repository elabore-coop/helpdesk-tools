# Copyright 2022 Stéphan Sainléger (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "helpdesk_portal_ticket_list",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Laetitia Da Costa",
    "license": "AGPL-3",
    "category": "Helpdesk",
    "summary": "Customize ticket portal view list",
    "description": "",
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
        "views/portal_ticket_view.xml",
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