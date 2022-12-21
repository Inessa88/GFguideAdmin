from django.utils import timezone
from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class SiteUsers(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email


class ProductPictures(models.Model):
    url = models.CharField(max_length=250)

    class Meta:
        db_table = "pictures"

    def __str__(self):
        return self.url


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE)

    class Meta:
        db_table = "restaurants"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    post_data = models.DateField(default=timezone.now)
    user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE)
    main_picture = models.ForeignKey(ProductPictures, on_delete=models.CASCADE, related_name='product_main_picuture')
    ingredient_picture = models.ForeignKey(ProductPictures, on_delete=models.CASCADE, related_name='product_ingredient_picuture')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name