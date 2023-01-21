from django.contrib import admin

from .models import User, Listing, Categories, Bid, Comments

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "start_bid", "creation", "creator")

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "author")

admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comments)