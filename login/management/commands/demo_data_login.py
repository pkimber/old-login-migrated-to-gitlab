from django.core.management.base import BaseCommand

from login.tests.model_maker import make_superuser
from login.tests.model_maker import make_user


class Command(BaseCommand):

    help = "Create demo data for 'login'"

    def handle(self, *args, **options):
        make_superuser('admin', 'admin')
        make_user('staff', 'staff', is_staff=True)
        make_user('web', 'web')
        print("Created 'login' demo data...")
