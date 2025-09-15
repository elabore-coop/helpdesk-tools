from odoo import Command, api, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    @api.onchange("task_id")
    def _onchange_task_id(self):
        for record in self:
            if record.timesheet_ids and record.task_id:
                not_yet_invoiced_timesheet_ids = [
                    t.id for t in record.timesheet_ids if not t.timesheet_invoice_id
                ]
                record.task_id.timesheet_ids = [
                    Command.link(t_id) for t_id in not_yet_invoiced_timesheet_ids
                ]
