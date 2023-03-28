from django.contrib import admin
from rango.models import Category, Page
from rango.models import MyUser, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class MyUserAdmin
    
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)