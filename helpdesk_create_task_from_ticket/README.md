================================
helpdesk_create_task_from_ticket
================================

This module changes the behavior of the buttons "create" and "create and edit" of the field `task` in a ticket form.

It automatically fills up these tasks fields

```
Ticket (helpdesk.ticke)     /   Tâche (project.task)

Intitulé (name)                 --> Titre (name)
Utilisateur assigné (user_id)   --> Assignés (user_ids)
Projet (project_id)             --> Projet (project_id)
Contact (partner_id)            --> Client (partner_id)
Catégorie (category_id)         --> service (service_id)
Request Type (request_type_id)  --> Type de demande (request_type_id)
Priorité (priority)             --> Priorité (priority)
```

# Installation

Use Odoo normal module installation procedure to install
`helpdesk_create_task_from_ticket`.

# Known issues / Roadmap

A current limitation is that one task can be linked to many tickets.
Thus, the above task fields are filled up at the creation of the task from a ticket form
but are not updated when the linked tickets are updated.

# Bug Tracker

Bugs are tracked on `our issues website <https://github.com/elabore-coop/helpdesk-tools/issues>`\_. In case of
trouble, please check there if your issue has already been
reported. If you spotted it first, help us smashing it by providing a
detailed and welcomed feedback.

# Credits

## Contributors

- Quentin Mondot

## Funders

The development of this module has been financially supported by:

- Elabore (https://elabore.coop)

## Maintainer

This module is maintained by Elabore.
