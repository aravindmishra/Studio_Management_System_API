# Generated by Django 2.1.7 on 2022-03-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='type',
        ),
        migrations.AddField(
            model_name='customerfilemapping',
            name='type',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
