# Generated by Django 4.0.4 on 2022-08-01 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0039_alter_submission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutthissubmission',
            name='purpose_chosen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purpose_chosen', to='SMMapp.purpose'),
        ),
    ]