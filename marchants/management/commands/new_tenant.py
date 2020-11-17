from django.core.management.base import BaseCommand
from django.utils import timezone
from marchants.models import Marchant

class Command(BaseCommand):
    help = 'creates new public tenant'

    def handle(self, *args, **kwargs):
        # create your public tenant
        user = Marchant.objects.create_user(email='admin@cyphertech.com.ng', password='awesome21')
        tenant = Shop(schema_name='public', name='zeus admin', user=user)
        tenant.save()

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'cyphertech.com.ng' # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()