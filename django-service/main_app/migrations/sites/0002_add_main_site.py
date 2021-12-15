from django.db import migrations
from main_app.keyconfig import Settings


def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    site = apps.get_model('sites', 'Site')
    site.objects.all().delete()

    # Register SITE_ID = 1
    site.objects.create(domain=Settings.SITE_DOMAIN, name=Settings.SITE_NAME)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sites)
    ]