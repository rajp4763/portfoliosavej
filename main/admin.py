from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from main.models import *
# Register your models here.

class QuiryAdmin(admin.ModelAdmin):
    search_fields=['name']
    ordering = ['created_on']
    list_filter=['status','created_on']
    list_display = ['name','created_on','status']


admin.site.register(Service)
admin.site.register(Work)
admin.site.register(AboutMe)
admin.site.register(Quiry,QuiryAdmin)