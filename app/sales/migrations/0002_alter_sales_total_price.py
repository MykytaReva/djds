# Generated by Django 4.1.2 on 2022-12-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
