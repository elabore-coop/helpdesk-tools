import odoo.http as http
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController


class HelpdeskTicketControllerPriority(HelpdeskTicketController):
    def _get_ticket_priorities(self):
        priorities = []
        for id, name in (
            http.request.env["helpdesk.ticket"]._fields["priority"].selection
        ):
            priorities.append({"id": id, "name": name})
        return priorities

    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        res = super(HelpdeskTicketControllerPriority, self).create_new_ticket(**kw)
        res.qcontext["priorities"] = self._get_ticket_priorities()
        return res

    def _prepare_submit_ticket_vals(self, **kw):
        res = super()._prepare_submit_ticket_vals(**kw)
        request_type = http.request.env["helpdesk.request.type"].browse(
            int(kw.get("request_type"))
        )
        res.update({"request_type_id": request_type.id})
        return res
