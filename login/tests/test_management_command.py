from django.test import TestCase
from login.management.commands.demo_data_login import Command


class TestComment(TestCase):

    def test_command(self):
        """
        Test the management command - make sure the database structure is still
        correct.
        """
        command = Command()
        command.handle()
