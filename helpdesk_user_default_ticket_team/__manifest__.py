# Copyright 2022 Stéphan Sainléger (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "helpdesk_user_default_ticket_team",
    "version": "16.0.1.1.0",
    "author": "Elabore",
    "website": "https://github.com/elabore-coop/helpdesk-tools",
    "maintainer": "Stéphan Sainléger",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Automate ticket team attribution when ticket created by portal user.",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/res_users_views.xml",
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
