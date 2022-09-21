from django.contrib import admin
from.models import Category, Dish, Showcase
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name','cat_image']
    list_editable = ['cat_name','cat_image']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','category_id','category','image','min','max','breakfast','lunch','dinner','drink','appetizer','price','dessert','in_stock','special']
    list_editable = ['special']
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Dish,DishAdmin)

@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ['id','show_name','show_txt','show_img']