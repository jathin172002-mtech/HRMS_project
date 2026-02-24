from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a default superuser if none exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@hrms.com',
                password='Admin@1234'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created: admin / Admin@1234'))
        else:
            self.stdout.write('ℹ️  Superuser already exists, skipping.')
