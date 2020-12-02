from django.core.management.base import BaseCommand
from django.utils import timezone
from marchants.models import Marchant
from tenant_users.tenants.utils import create_public_tenant
from tenant_users.tenants.tasks import provision_tenant

class Command(BaseCommand):
    help = 'creates new public tenant'

    def handle(self, *args, **kwargs):
        # create your public tenant
        create_public_tenant("cyphertech.com.ng", "admin@cyphertech.com.ng")
        Marchant.objects.create_user(email='chuks@cyphertech.com.ng', password='awesome21', is_active=True, is_staff=True)
        provision_tenant("Chukstore", "chukstore", "chuks@cyphertech.com.ng", is_staff=True)
        Marchant.objects.create_user(email='maki@cyphertech.com.ng', password='awesome21', is_active=True, is_staff=True)
        fdqn = provision_tenant("Makistore", "makistore", "maki@cyphertech.com.ng", is_staff=True)
        print('Done')
        print(fdqn)
        # tenant = Shop(schema_name='public', name='zeus-admin', user=user)
        # tenant.save()

        # # Add one or more domains for the tenant
        # domain = Domain()
        # domain.domain = 'cyphertech.com.ng' # don't add your port or www here! on a local server you'll want to use localhost here
        # domain.tenant = tenant
        # domain.is_primary = True
        # domain.save()