# Generated by Django 4.1.2 on 2022-12-06 10:38

import customers.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('logo', models.ImageField(default='logo/anonymous.png', upload_to=customers.models.customer_logo, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
            ],
        ),
    ]
