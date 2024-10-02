from odoo import models, fields


class RequestType(models.Model):
    _name = "helpdesk.request.type"
    _description = "Request Type"

    name = fields.Char('name', required=True)
    sequence = fields.Integer()