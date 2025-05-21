from odoo import _, api, fields, models

class Users(models.Model):
    _inherit = "res.users"

    default_helpdesk_ticket_team_id = fields.Many2one('helpdesk.ticket.team', string='Default Helpdesk Team')
