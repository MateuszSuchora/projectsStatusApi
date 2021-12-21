from django.contrib import admin

# Register your models here.
from .models import Repo


class PpeAdmin(admin.ModelAdmin):  # its adder
    list_display = ('name', 'owner', 'is_private')
    search_fields = ('name', 'owner',)


admin.site.register(Repo, PpeAdmin)
