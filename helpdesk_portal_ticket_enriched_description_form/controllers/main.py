import odoo.http as http
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController


class HelpdeskTicketControllerDescription(HelpdeskTicketController):
    def _prepare_submit_ticket_vals(self, **kw):
        res = super()._prepare_submit_ticket_vals(**kw)
        description = ""
        if kw.get("small_description", False):
            description = (
                description + "<b>DESCRIPTION:</b><br/>" + kw["small_description"]
            )
            del kw["small_description"]
        if kw.get("access", False):
            description = description + "<br/><br/><b>ACCESS:</b><br/>" + kw["access"]
            del kw["access"]
        if kw.get("bug_report", False):
            description = (
                description + "<br/><br/><b>BUG REPORT:</b><br/>" + kw["bug_report"]
            )
            del kw["bug_report"]
        res.update({"description": description})
        return res
