# Generated by Django 3.1.4 on 2021-01-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoBase', '0004_auto_20210108_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descrtodo',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]