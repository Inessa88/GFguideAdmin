from django.utils import timezone
from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SiteUsers(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class ProductPictures(models.Model):
    url = models.CharField(max_length=250)

    class Meta:
        db_table = "pictures"
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    def __str__(self):
        return self.url


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE)

    class Meta:
        db_table = "restaurants"
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    post_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE, null=True, blank=True)
    main_picture = models.ForeignKey(ProductPictures, on_delete=models.CASCADE, related_name='product_main_picture')
    # ingredient_picture = models.ForeignKey(ProductPictures, on_delete=models.CASCADE, related_name='product_ingredient_picture')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name