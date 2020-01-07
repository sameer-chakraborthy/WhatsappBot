from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = ('name','created')
    list_filter = ('created')


admin.site.register(Table,TableAdmin)
admin.site.unregister(Group)

