# Generated by Django 4.0.4 on 2022-07-05 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0004_remove_approvalflow_submission_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvalflow',
            name='submission_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='approval_flow_submission_type', to='SMMapp.submissiontype'),
            preserve_default=False,
        ),
    ]