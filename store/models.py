from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return f"The category name {self.name_category}"


class Product(models.Model):
    name_product = models.CharField(max_length=50)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"the {self.name_product} coast : {self.price} $ ."
