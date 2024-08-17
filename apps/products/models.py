from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/')

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
