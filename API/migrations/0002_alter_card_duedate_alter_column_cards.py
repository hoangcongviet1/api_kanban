# Generated by Django 5.0.6 on 2024-11-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='cards',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
