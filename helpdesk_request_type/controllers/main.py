import odoo.http as http
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

class HelpdeskTicketControllerRequestType(HelpdeskTicketController):

    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        categories = http.request.env["helpdesk.ticket.category"].search(
            [("active", "=", True)]
        )
        request_types = http.request.env["helpdesk.request.type"].search([])
        email = http.request.env.user.email
        name = http.request.env.user.name
        return http.request.render(
            "helpdesk_mgmt.portal_create_ticket",
            {
                "categories": categories,
                "teams": self._get_teams(),
                "email": email,
                "name": name,
                "request_types": request_types
            },
        )

    def _prepare_submit_ticket_vals(self, **kw):
        res = super()._prepare_submit_ticket_vals(**kw)
        request_type = http.request.env["helpdesk.request.type"].browse(
            int(kw.get("request_type"))
        )
        res.update({"request_type_id": request_type.id})
        return res