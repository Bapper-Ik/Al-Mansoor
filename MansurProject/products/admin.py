from django.contrib import admin
from .models import Product, Shoes, Atampa, Comments


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'yards')


class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'status')


class AtampaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'customer_name', 'customer_subject')


admin.site.register(Product, ProductAdmin)

admin.site.register(Shoes, ShoesAdmin)

admin.site.register(Atampa, AtampaAdmin)

admin.site.register(Comments, CommentsAdmin)
