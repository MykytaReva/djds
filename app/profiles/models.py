from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


def avatars(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio')
    avatar = models.ImageField(
        upload_to=avatars,
        default='avatar/anonymous.png',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
