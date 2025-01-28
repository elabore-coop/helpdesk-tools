import odoo.http as http
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

class HelpdeskTicketControllerRequestType(HelpdeskTicketController):

    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        res = super(HelpdeskTicketControllerRequestType, self).create_new_ticket(**kw)
        request_types = http.request.env["helpdesk.request.type"].search([])
        res.qcontext["request_types"] = request_types
        return res

    def _prepare_submit_ticket_vals(self, **kw):
        res = super()._prepare_submit_ticket_vals(**kw)
        request_type = http.request.env["helpdesk.request.type"].browse(
            int(kw.get("request_type"))
        )
        res.update({"request_type_id": request_type.id})
        return res