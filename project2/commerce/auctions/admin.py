from django.contrib import admin

from .models import User, Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "start_bid", "creation")

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)