from odoo import  api, fields, models, tools

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("team_id") and vals.get("partner_id"):
                partner = self.env["res.partner"].browse(vals.get("partner_id"))
                if not partner:
                    continue
                user = self.env["res.users"].browse(partner.user_ids[0].id)
                if not user:
                    continue
                if user.default_helpdesk_ticket_team_id:
                    vals["team_id"] = user.default_helpdesk_ticket_team_id.id

        return super().create(vals_list)
