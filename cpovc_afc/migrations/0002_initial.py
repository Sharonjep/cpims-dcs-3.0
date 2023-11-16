# Generated by Django 4.1.7 on 2023-10-30 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_forms', '0001_initial'),
        ('cpovc_afc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccaserecord'),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
