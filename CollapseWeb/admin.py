from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Client, ClientLoader

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

# admin.site.register(Client, ClientAdmin)

class ClientLoaderAdmin(ModelAdmin):
    @admin.action(description='Mark selected clients as hidden')
    def client_make_hidden(modeladmin, request, queryset):
        queryset.update(show_in_loader=False)


    @admin.action(description='Mark selected clients as visible')
    def client_make_visible(modeladmin, request, queryset):
        queryset.update(show_in_loader=True)

    list_display = ('name', 'version', 'category', 'filename', 'id', 'show_in_loader', 'working', 'internal')
    list_filter = ('version', )
    search_fields = ('name__startswith',)
    actions = [client_make_hidden, client_make_visible]

admin.site.register(ClientLoader, ClientLoaderAdmin)