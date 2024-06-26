# Generated by Django 4.2.9 on 2024-01-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monitoring", "0033_alter_monitoredresource_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationcheck",
            name="metrics",
            field=models.ManyToManyField(
                related_name="+",
                through="monitoring.NotificationMetricDefinition",
                to="monitoring.metric",
            ),
        ),
    ]
