from django.contrib import admin
from .models import (
    ProductCategory,
    SiteUsers,
    ProductPictures,
    Restaurants,
    Products
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory

@admin.register(SiteUsers)
class SiteUsersAdmin(admin.ModelAdmin):
    model = SiteUsers

@admin.register(ProductPictures)
class ProductPicturesAdmin(admin.ModelAdmin):
    model = ProductPictures

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    model = Restaurants

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name', 'post_date', 'user', 'category')

