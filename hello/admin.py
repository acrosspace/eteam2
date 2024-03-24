from django.contrib import admin

# Register your models here.

from .models import Hello

@admin.register(Hello)
class HelloAdmin(admin.ModelAdmin):
    pass
    #list_display = ('name', 'description', 'created_date', 'contact_email', 'is_active')
    #list_filter = ['created_date']
    #search_fields = ['name', 'description']