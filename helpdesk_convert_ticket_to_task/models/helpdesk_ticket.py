from odoo import _, models, api

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def button_convert_to_task(self):
        user_ids = [self.user_id.id]
        task_service_id, request_type_id = self._match_task_service_and_request_type(
            ticket_category_id=self.category_id.id,
            ticket_request_type_id=self.request_type_id.id
        )

        task = self.env["project.task"].create({
            "name": self.name,
            "description": self.description,
            "project_id": self.project_id.id,
            "user_ids": user_ids,
            "partner_id": self.partner_id.id,
            "service_id": task_service_id,
            "request_type_id": request_type_id,
            "priority": self.priority
        })

        # copy chatter
        for msg in reversed(self.message_ids):
            msg.copy({
                'model': 'project.task',
                'res_id': task.id
            })

            # copy attachments inserted in the messages
            for attach in msg.attachment_ids:
                attach.copy({
                    'res_model': 'project.task',
                    'res_id': task.id,
                    'res_name': task.name
                })

        # copy attachments not added in a message
        for attachment in self.attachment_ids:
            attachment.copy({
                'res_model': 'project.task',
                'res_id': task.id,
                'res_name': task.name
            })

        # copy subscribers
        task.message_subscribe(partner_ids=self.message_partner_ids.ids)

        # warn (in the chatter) that the task is a copy
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        ticket_url = f"{base_url}/web#id={self.id}&model=helpdesk.ticket&view_type=form"
        task_message = _(
            "This task has been converted from a ticket. You can find the original ticket <a href='%(ticket_url)s' target='_blank'>on this link</a>.",
            ticket_url=ticket_url
        )
        task.message_post(body=task_message)

        # warn (in the chatter) that the ticket has been converted
        task_url = f"{base_url}/web#id={task.id}&model=project.task&view_type=form"
        ticket_message = _(
            "This ticket has been converted into a task. You can find it <a href='%(task_url)s' target='_blank'>on this link</a>.",
            task_url=task_url
        )
        self.message_post(body=ticket_message)

        # archive the ticket
        self.write({
            "active": False,
            "task_id": task.id
        })
        # transfer timesheets from ticket to task
        self._onchange_task_id()

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "target": "current",
            "res_model": "project.task",
            "res_id": task.id,
        }

    def _match_task_service_and_request_type(
            self,
            ticket_category_id: int,
            ticket_request_type_id: int
    ) -> tuple[int, int]:
        """
        This function permits to match the task service_id and request_type from the ticket category and request type
        """
        helpdesk_ticket_category = self.env["helpdesk.ticket.category"].search(
            [("id", "=", ticket_category_id)],
            limit=1
        )
        task_service = self.env["task.service"].search([("name", "=", helpdesk_ticket_category.name)])

        helpdesk_ticket_request_type = self.env["helpdesk.request.type"].search(
            [("id", "=", ticket_request_type_id)],
            limit=1
        )
        task_request_type = self.env["request.type"].search([("name", "=", helpdesk_ticket_request_type.name)])

        return task_service.id, task_request_type.id
