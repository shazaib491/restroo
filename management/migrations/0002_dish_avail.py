# Generated by Django 3.0.8 on 2020-07-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='avail',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]