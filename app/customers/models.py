from django.core.validators import FileExtensionValidator
from django.db import models


def customer_logo(instance, filename):
    return 'logo/{0}/{1}'.format(instance.name, filename)


class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(
        upload_to=customer_logo,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        default='logo/anonymous.png'
    )

    def __str__(self):
        return str(self.name)
