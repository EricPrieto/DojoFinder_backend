from django.contrib import admin
from .models import School

# Register your models here.
admin.site.register(School)
# admin.site.register(Rating)



# class SchoolAdmin(admin.ModelAdmin):
#     list_display =['school_name', 'school_description']
#     list_filter =['school_type']