from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Employee)


from rangefilter.filter import DateRangeFilter

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_at', DateRangeFilter), ('updated_at', DateRangeFilter),
    )