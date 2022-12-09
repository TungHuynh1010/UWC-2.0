# Generated by Django 4.1.3 on 2022-12-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('phone_num', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=50)),
                ('curr_status', models.CharField(choices=[('busy', 'busy'), ('available', 'available')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.FloatField()),
                ('curr_status', models.CharField(choices=[('busy', 'busy'), ('available', 'available')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('capacity', models.FloatField()),
                ('fuel_capacity', models.FloatField()),
                ('curr_status', models.CharField(choices=[('busy', 'busy'), ('available', 'available')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_day', models.DateField(unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('weight__gt', 0)), name='Weight must greater than zero'),
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('capacity__gt', 0)), name='Capacity must greater than zero'),
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('fuel_capacity__gt', 0)), name='Fuel capacity must greater than zero'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workday',
            field=models.ManyToManyField(blank=True, default=None, to='src.workday'),
        ),
    ]