# Generated by Django 4.1.3 on 2022-12-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_remove_employee_mission_employee_mission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='MCP',
        ),
        migrations.AddField(
            model_name='mission',
            name='MCP',
            field=models.ManyToManyField(blank=True, null=True, to='src.mcp'),
        ),
    ]
