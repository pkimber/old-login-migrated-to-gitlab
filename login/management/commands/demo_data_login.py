from django.core.management.base import BaseCommand

from login.tests.scenario import (
    user_contractor,
    user_default,
)


class Command(BaseCommand):

    help = "Create demo data for 'login'"

    def handle(self, *args, **options):
        user_contractor()
        user_default()
        print("Created 'login' demo data...")
