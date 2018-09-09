# Generated by Django 2.0.7 on 2018-09-09 18:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import ekotab.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('SUBMITTED', 'Submitted'), ('FAILED', 'Failed'), ('PASSED', 'Passed')], default=ekotab.models.Statuses('Ongoing'), max_length=9)),
                ('date_added', models.DateField(default=datetime.date.today, verbose_name='date added')),
                ('date_submitted', models.DateField(blank=True, null=True, verbose_name='date submitted')),
                ('is_current_step', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='ekotab.Student'),
        ),
    ]
