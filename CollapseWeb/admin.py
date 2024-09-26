from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import *


class ClientAdmin(ModelAdmin):
    @admin.action(description='Mark selected clients as hidden')
    def client_make_hidden(modeladmin, _, queryset):
        queryset.update(show_in_loader=False)

    @admin.action(description='Mark selected clients as visible')
    def client_make_visible(modeladmin, _, queryset):
        queryset.update(show_in_loader=True)

    list_display = ('name', 'version', 'filename', 'id', 'show_in_loader', 'working', 'internal')
    list_filter = ('version', )
    search_fields = ('name__startswith',)
    actions = [client_make_hidden, client_make_visible]


class FabricClientAdmin(ModelAdmin):
    @admin.action(description='Mark selected clients as hidden')
    def client_make_hidden(modeladmin, _, queryset):
        queryset.update(show_in_loader=False)

    @admin.action(description='Mark selected clients as visible')
    def client_make_visible(modeladmin, _, queryset):
        queryset.update(show_in_loader=True)

    list_display = ('name', 'version', 'filename', 'id', 'show_in_loader', 'working')
    list_filter = ('name', )
    search_fields = ('name__startswith',)
    actions = [client_make_hidden, client_make_visible]


class MessageAdmin(ModelAdmin):
    list_display = ('id', 'type', 'body', 'hidden', 'post_at')


class ConfigAdmin(ModelAdmin):
    list_display = ('client', 'file', 'config_path')

admin.site.register(Client, ClientAdmin)
admin.site.register(FabricClient, FabricClientAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(CreditsText)