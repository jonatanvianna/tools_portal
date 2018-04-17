from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            # email, password
            User.objects.create_superuser(username='admin', email="admin@jonatan.pw", password="passwd123")
