# helpdesk_convert_ticket_to_task

This module changes the behavior of the buttons "create" and "create and edit" of the
field `task` in a ticket form.

It automatically fills up many fields (check the function button_convert_to_task for details)

# Installation

Use Odoo normal module installation procedure to install
`helpdesk_convert_ticket_to_task`.

# Known issues / Roadmap

A current limitation is that one task can be linked to many tickets. Thus, the above
task fields are filled up at the creation of the task from a ticket form but are not
updated when the linked tickets are updated.

# Bug Tracker

Bugs are tracked on
`our issues website <https://github.com/elabore-coop/helpdesk-tools/issues>`\_. In case
of trouble, please check there if your issue has already been reported. If you spotted
it first, help us smashing it by providing a detailed and welcomed feedback.

# Credits

## Contributors

- Quentin Mondot

## Funders

The development of this module has been financially supported by:

- Elabore (https://elabore.coop)

## Maintainer

This module is maintained by Elabore.
