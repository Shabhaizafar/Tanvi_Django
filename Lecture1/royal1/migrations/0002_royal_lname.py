# Generated by Django 5.2 on 2025-05-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royal1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='royal',
            name='lname',
            field=models.CharField(null=True),
        ),
    ]
