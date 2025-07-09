from collections import OrderedDict
from operator import itemgetter

from odoo import _, http
from odoo.http import request
from odoo.osv.expression import AND
from odoo.tools import groupby as groupbyelem

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortalHelpdesk(CustomerPortal):
    _inherit = "helpdesk_mgmt.myaccount"

    @http.route(
        ["/my/tickets", "/my/tickets/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_tickets(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in=None,
        groupby=None,
        **kw,
    ):
        HelpdeskTicket = request.env["helpdesk.ticket"]
        # Avoid error if the user does not have access.
        if not HelpdeskTicket.check_access_rights("read", raise_exception=False):
            return request.redirect("/my")

        values = self._prepare_portal_layout_values()

        searchbar_sortings = self._ticket_get_searchbar_sortings()
        searchbar_sortings = dict(
            sorted(
                self._ticket_get_searchbar_sortings().items(),
                key=lambda item: item[1]["sequence"],
            )
        )

        searchbar_filters = {
            "all": {"label": _("All"), "domain": []},
            "closed": {"label": _("Ouvert"), "domain": [("closed", "=", False)]},
        }
        for stage in request.env["helpdesk.ticket.stage"].search([]):
            searchbar_filters[str(stage.id)] = {
                "label": stage.name,
                "domain": [("stage_id", "=", stage.id)],
            }

        searchbar_inputs = self._ticket_get_searchbar_inputs()
        searchbar_groupby = self._ticket_get_searchbar_groupby()

        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        if not filterby:
            filterby = "closed"
        domain = searchbar_filters.get(filterby, searchbar_filters.get("all"))["domain"]

        if not groupby:
            groupby = "stage"

        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        if not search_in:
            search_in = "all"
        if search:
            domain += self._ticket_get_search_domain(search_in, search)

        domain = AND(
            [
                domain,
                request.env["ir.rule"]._compute_domain(HelpdeskTicket._name, "read"),
            ]
        )

        # count for pager
        ticket_count = HelpdeskTicket.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/tickets",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "groupby": groupby,
                "search": search,
                "search_in": search_in,
            },
            total=ticket_count,
            page=page,
            step=self._items_per_page,
        )

        order = self._ticket_get_order(order, groupby)
        tickets = HelpdeskTicket.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager["offset"],
        )
        request.session["my_tickets_history"] = tickets.ids[:100]

        groupby_mapping = self._ticket_get_groupby_mapping()
        group = groupby_mapping.get(groupby)
        if group:
            grouped_tickets = [
                request.env["helpdesk.ticket"].concat(*g) for k, g in groupbyelem(tickets, itemgetter(group))
            ]
        elif tickets:
            grouped_tickets = [tickets]
        else:
            grouped_tickets = []

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "grouped_tickets": grouped_tickets,
                "page_name": "ticket",
                "default_url": "/my/tickets",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "search": search,
                "sortby": sortby,
                "groupby": groupby,
                "searchbar_filters": OrderedDict(sorted(searchbar_filters.items())),
                "filterby": filterby,
            }
        )
        return request.render("helpdesk_mgmt.portal_my_tickets", values)
