# Generated by Django 4.0.4 on 2022-07-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0009_remove_header_contractor_logo_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='contractor_logo_1',
            field=models.TextField(blank=True, null=True, verbose_name='Contractor logo'),
        ),
    ]