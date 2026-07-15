# portal/admin.py
from django.contrib import admin
from .models import Profile, LostItem, FoundItem, ItemHistory

# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'contact', 'gender', 'location')
    search_fields = ('user__username', 'full_name', 'email', 'contact')
    list_filter = ('gender',)

# Lost Item Admin
@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'user', 'is_claimed', 'returned', 'date_lost')
    search_fields = ('title', 'description', 'location', 'user__username')
    list_filter = ('category', 'is_claimed', 'returned', 'date_lost')

# Found Item Admin
@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'user', 'is_claimed', 'returned', 'date_found')
    search_fields = ('title', 'description', 'location', 'user__username')
    list_filter = ('category', 'is_claimed', 'returned', 'date_found')

# Item History Admin
@admin.register(ItemHistory)
class ItemHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'original_user', 'item_type', 'date_posted', 'date_returned')
    search_fields = ('title', 'description', 'location', 'original_user__username')
    list_filter = ('category', 'item_type', 'date_posted', 'date_returned')
