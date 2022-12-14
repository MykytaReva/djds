from django.core.validators import FileExtensionValidator
from django.db import models
from profiles.models import Profile


def report(instance, filename):
    return "report/{0}/{1}".format(instance.name, filename)


class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=report,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        blank=True
    )
    remarks = models.TextField(default='No remarks')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
