import odoo.http as http
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController


class HelpdeskTicketControllerRequestType(HelpdeskTicketController):
    def _get_ticket_request_types(self):
        types = []
        for type in http.request.env["helpdesk.request.type"].search([]):
            types.append({"id": type.id, "name": type.name})
        return types

    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        res = super(HelpdeskTicketControllerRequestType, self).create_new_ticket(**kw)
        res.qcontext["request_types"] = self._get_ticket_request_types()
        return res

    def _prepare_submit_ticket_vals(self, **kw):
        res = super()._prepare_submit_ticket_vals(**kw)
        request_type = http.request.env["helpdesk.request.type"].browse(
            int(kw.get("request_type"))
        )
        res.update({"request_type_id": request_type.id})
        return res
