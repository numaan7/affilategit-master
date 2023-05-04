from django.contrib import admin
from .models import Product, Blog, CustomerQuery, Service

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    
admin.site.register(Product, ProductAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    
admin.site.register(Blog, BlogAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Service, ServiceAdmin)

class CustomerQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    
admin.site.register(CustomerQuery, CustomerQueryAdmin)