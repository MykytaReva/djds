# Generated by Django 4.1.2 on 2022-12-06 10:48

import django.core.validators
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(default='product/nothing.png', upload_to=products.models.product_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('price', models.FloatField(help_text='in USD')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]