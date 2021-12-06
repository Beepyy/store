from django.contrib import admin
from .models import *

class Basket_inlines(admin.TabularInline):
    model=Basket

class Goods_descr_inlines(admin.TabularInline):
    model=Goods_descr

class Goods_inlines(admin.TabularInline):
    model=Goods

class Products_inlines(admin.TabularInline):
    model=Product

@admin.register(Goods)    
class GoodsAdmin(admin.ModelAdmin):
    list_display=("name_of_good","price","amount","catalog")
    inlines=[Goods_descr_inlines]

@admin.register(Profile)    
class ProfileAdmin(admin.ModelAdmin):
    list_display=("user",)
    inlines=[Basket_inlines]

@admin.register(Catalogs)
class CatalogsAdmin(admin.ModelAdmin):
    inlines=[Goods_inlines]

@admin.register(Basket)
class Basket_admin(admin.ModelAdmin):
    inlines=[Products_inlines]

@admin.register(Bought)
class Boght_admin(admin.ModelAdmin):
    inlines=[Products_inlines]    
admin.site.register(Product)
admin.site.register(Goods_descr)