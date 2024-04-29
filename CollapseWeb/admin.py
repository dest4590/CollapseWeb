from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    @admin.action(description='Mark selected clients as hidden')
    def client_make_hidden(modeladmin, request, queryset):
        queryset.update(hidden=True)


    @admin.action(description='Mark selected clients as visible')
    def client_make_visible(modeladmin, request, queryset):
        queryset.update(hidden=False)

    list_display = ('name', 'version', 'link', 'id', 'created_at', 'updated_at', 'hidden')
    list_filter = ('version', )
    search_fields = ('name__startswith',)
    actions = [client_make_hidden, client_make_visible]

admin.site.register(Client, ClientAdmin)