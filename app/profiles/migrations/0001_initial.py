# Generated by Django 4.1.2 on 2022-12-06 11:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='No bio')),
                ('avatar', models.ImageField(default='avatar/anonymous.png', upload_to=profiles.models.avatars, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
