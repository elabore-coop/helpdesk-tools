from odoo import models, api


class ProjectTask(models.Model):
    """
    The function "create" is overloaded to adapt the fields "priority" and "user_ids" from the context of helpdesk.ticket to the one of project.task
    This function is called when the user clicks on the button "create" in the task field of the ticket form
    The function "onchange" is overloaded to adapt the fields "priority" and user_ids from the context of helpdesk.ticket to the one of project.task
    This function is called when the user clicks on the button "create and modify" in the task field of the ticket form
    """
    _inherit = "project.task"

    @api.model
    def create(self, vals_list):
        if self.env.context["default_priority"] == "3":
            priority = "1"
        else:
            priority = "0"
        user_ids = [self.env.context["default_user_ids"]]
        result = super(ProjectTask, self.with_context(
            default_priority=priority,
            default_user_ids=user_ids
        )).create(vals_list)
        return result

    def onchange(self, values, field_name, field_onchange):
        if self.env.context["default_priority"] == "3":
            priority = "1"
        else:
            priority = "0"
        user_ids = [self.env.context["default_user_ids"]]
        result = super(ProjectTask, self.with_context(
            default_priority=priority,
            default_user_ids=user_ids
        )).onchange(values, field_name, field_onchange)

        return result
