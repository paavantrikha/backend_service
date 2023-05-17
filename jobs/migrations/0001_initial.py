# Generated by Django 4.2 on 2023-04-22 16:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('minimim_salary', models.IntegerField(default=0)),
                ('maximum_salary', models.IntegerField(default=0)),
                ('target_date_to_finish_hiring', models.DateField(blank=True, null=True)),
                ('job_description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='JobApplicationModel',
            fields=[
                ('application_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidatemodel')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobmodel')),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
            },
        ),
    ]
