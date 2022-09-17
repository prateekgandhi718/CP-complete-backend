
from django.db import models

from django.utils.translation import gettext_lazy as _



def upload_to(instance, filename):
    return f'{filename}'

# Create your models here.
#creating model for list of factories
class Factory(models.Model):
    # by default the models are gonna create the ID value in integers. you could use UUID as well. 
    factory_name = models.CharField(max_length=100)
    factory_location = models.CharField(max_length=100)

    def __str__(self):
        return self.factory_name


class Product(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null = True, related_name="productsInFactory")
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1000, null = True, blank=True)

    image = models.ImageField(_("Image"), upload_to = upload_to,  null = True, blank=True, default = 'posts/default.png')

    def __str__(self):
        return f'{self.title}'


