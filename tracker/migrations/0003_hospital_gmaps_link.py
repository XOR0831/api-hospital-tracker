# Generated by Django 3.2.3 on 2021-05-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20210526_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='gmaps_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]