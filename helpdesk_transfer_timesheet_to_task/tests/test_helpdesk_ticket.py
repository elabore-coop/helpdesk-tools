from odoo.tests.common import TransactionCase


class TestHelpdeskTicket(TransactionCase):

    def setUp(self):
        super(TestHelpdeskTicket, self).setUp()
        self.HelpdeskTicket = self.env["helpdesk.ticket"]
        self.ProjectTask = self.env["project.task"]
        self.AccountAnalyticLine = self.env["account.analytic.line"]
        self.AccountMove = self.env["account.move"]
        self.Project = self.env["project.project"]

        self.project = self.Project.create(
            {"name": "Test project", "allow_timesheets": True}
        )
        self.analytic_account = self.project.analytic_account_id
        # Create a sample task
        self.task = self.ProjectTask.create(
            {"name": "Sample Task", "project_id": self.project.id}
        )

    def test_timesheet_added_to_linked_task(self):
        # Create a ticket
        ticket = self.HelpdeskTicket.create(
            {"name": "Test Ticket", "description": "My ticket"}
        )

        # Associate a task with the ticket
        ticket.task_id = self.task.id

        # Log time on the ticket
        timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Time Entry",
                "ticket_id": ticket.id,
                "unit_amount": 1.0,
                "account_id": self.analytic_account.id,
            }
        )

        timesheet.onchange_ticket_id()

        # Check that timesheet is linked to the task
        self.assertIn(timesheet, self.task.timesheet_ids)

    def test_timesheet_added_to_new_task(self):
        # Create a ticket
        ticket = self.HelpdeskTicket.create(
            {"name": "Test Ticket", "description": "My ticket"}
        )

        # Log time on the ticket
        timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Time Entry",
                "ticket_id": ticket.id,
                "unit_amount": 1.0,
                "account_id": self.analytic_account.id,
            }
        )

        # Associate a task with the ticket
        ticket.task_id = self.task.id
        ticket._onchange_task_id()

        # Check that timesheet is linked to the task
        self.assertIn(timesheet, self.task.timesheet_ids)

    def test_timesheet_for_task_linked_to_several_tickets(self):
        # Create a first ticket
        ticket_1 = self.HelpdeskTicket.create(
            {"name": "Test Ticket 1", "description": "My 1st ticket"}
        )

        # Log time on the first ticket
        first_timesheet = self.AccountAnalyticLine.create(
            {
                "name": "First Time Entry",
                "ticket_id": ticket_1.id,
                "unit_amount": 1.0,
                "account_id": self.analytic_account.id,
            }
        )
        # Associate a task to the first ticket
        ticket_1.task_id = self.task.id
        ticket_1._onchange_task_id()
        # Create a second ticket
        ticket_2 = self.HelpdeskTicket.create(
            {"name": "Test Ticket 2", "description": "My 2nd ticket"}
        )
        # Log time on the second ticket
        second_timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Second Time Entry",
                "ticket_id": ticket_2.id,
                "unit_amount": 2.0,
                "account_id": self.analytic_account.id,
            }
        )
        # Associate the same task to the second ticket
        ticket_2.task_id = self.task.id
        ticket_2._onchange_task_id()

        # Check that both timesheets are linked to the task
        self.assertIn(first_timesheet, self.task.timesheet_ids)
        self.assertIn(second_timesheet, self.task.timesheet_ids)

    def test_timesheet_moved_between_tasks(self):
        # Create a second task
        task_2 = self.ProjectTask.create(
            {"name": "Second Task", "project_id": self.project.id}
        )

        # Create a ticket
        ticket = self.HelpdeskTicket.create(
            {"name": "Test Ticket", "description": "My ticket"}
        )

        # Log time on the ticket
        timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Time Entry for Moving",
                "ticket_id": ticket.id,
                "unit_amount": 1.0,
                "account_id": self.analytic_account.id,
            }
        )

        # Associate the first task with the ticket
        ticket.task_id = self.task.id
        ticket._onchange_task_id()

        # Associate the second task with the ticket
        ticket.task_id = task_2.id
        ticket._onchange_task_id()

        # Check if timesheet is moved to the second task
        self.assertNotIn(timesheet, self.task.timesheet_ids)
        self.assertIn(timesheet, task_2.timesheet_ids)

    def test_timesheet_already_invoiced_are_not_moved(self):
        journal = self.env["account.journal"].create(
            {"name": "My journal", "code": "test", "type": "bank"}
        )
        account_move = self.AccountMove.create(
            {"move_type": "entry", "journal_id": journal.id}
        )
        # Create a ticket
        ticket = self.HelpdeskTicket.create(
            {"name": "Test Ticket", "description": "My ticket"}
        )

        # Log already invoiced timesheet on the ticket
        already_invoiced_timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Already Invoiced Time Entry",
                "ticket_id": ticket.id,
                "unit_amount": 1.0,
                "account_id": self.analytic_account.id,
                "timesheet_invoice_id": account_move.id,
            }
        )

        # Log not invoiced timesheet on the ticket
        not_invoiced_timesheet = self.AccountAnalyticLine.create(
            {
                "name": "Not Invoiced Time Entry",
                "ticket_id": ticket.id,
                "unit_amount": 2.0,
                "account_id": self.analytic_account.id,
            }
        )

        # Associate a task with the ticket
        ticket.task_id = self.task.id
        ticket._onchange_task_id()

        # Check already invoiced timesheet has not been moved
        self.assertNotIn(already_invoiced_timesheet, self.task.timesheet_ids)
        self.assertIn(not_invoiced_timesheet, self.task.timesheet_ids)
