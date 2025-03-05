from odoo import models, api


class ProjectTask(models.Model):
    """
    The function "create" is overloaded to adapt the field "user_ids" from the context of helpdesk.ticket to the one of project.task
    This function is called when the user clicks on the button "create" in the task field of the ticket form
    The function "onchange" is overloaded to adapt the field "user_ids" from the context of helpdesk.ticket to the one of project.task
    This function is called when the user clicks on the button "create and modify" in the task field of the ticket form
    """
    _inherit = "project.task"

    @api.model
    def create(self, vals_list):
        if all(key in self.env.context for key in (
                "default_user_id",
                "default_ticket_category_id",
                "default_ticket_request_type_id"
        )):
            user_ids = [self.env.context["default_user_id"]]
            task_service_id, request_type_id = self._match_task_service_and_request_type(
                ticket_category_id=self.env.context["default_ticket_category_id"],
                ticket_request_type_id=self.env.context["default_ticket_request_type_id"]
            )

            return super(ProjectTask, self.with_context(
                default_user_ids=user_ids,
                default_service_id=task_service_id,
                default_request_type_id=request_type_id
            )).create(vals_list)

        return super(ProjectTask, self).create(vals_list)

    def onchange(self, values, field_name, field_onchange):
        if all(key in self.env.context for key in (
                "default_user_id",
                "default_ticket_category_id",
                "default_ticket_request_type_id"
        )):
            user_ids = [self.env.context["default_user_id"]]
            task_service_id, request_type_id = self._match_task_service_and_request_type(
                ticket_category_id=self.env.context["default_ticket_category_id"],
                ticket_request_type_id=self.env.context["default_ticket_request_type_id"]
            )

            return super(ProjectTask, self.with_context(
                default_user_ids=user_ids,
                default_service_id=task_service_id,
                default_request_type_id=request_type_id
            )).onchange(values, field_name, field_onchange)

        return super(ProjectTask, self).onchange(values, field_name, field_onchange)

    def _match_task_service_and_request_type(
            self,
            ticket_category_id: int,
            ticket_request_type_id: int
    ) -> tuple[int, int]:
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
