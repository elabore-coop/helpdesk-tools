from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    request_type_id = fields.Many2one('helpdesk.request.type', string='Request Type')