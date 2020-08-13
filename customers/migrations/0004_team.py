# Generated by Django 3.0.8 on 2020-08-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('designation', models.CharField(blank=True, max_length=10, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
                ('fb', models.URLField(blank=True, null=True)),
                ('twt', models.URLField(blank=True, null=True)),
                ('insta', models.URLField(blank=True, null=True)),
            ],
        ),
    ]