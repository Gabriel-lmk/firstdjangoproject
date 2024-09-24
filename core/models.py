from django.db import models
from unicodedata import decimal


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantity in Stock')
    image = models.ImageField('Image', upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    lastname = models.CharField('Lastname', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.name} {self.lastname}'