from django.core.validators import FileExtensionValidator
from django.db import models


def product_image(instance, filename):
    return 'product/{0}/{1}'.format(instance.name, filename)


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=product_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        default='product/nothing.png'
    )
    price = models.FloatField(help_text='in USD')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d.%m.%Y')}"