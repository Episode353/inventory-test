from django.contrib import admin
from .models import Profile, Item, Set, Bundle, Character

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'essence', 'bio')
    search_fields = ('user__username', 'bio')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'character', 'set')
    search_fields = ('name', 'description')
    list_filter = ('character', 'set')

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')
    search_fields = ('name', 'profile__user__username')
    list_filter = ('profile',)

