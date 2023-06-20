from django.contrib import admin
from .models import User, Posts, UserProfile

# Register your models here.



admin.site.register(User)


admin.site.register(UserProfile)


class PostsAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Posts._meta.get_fields()]
    list_display = ('author', 'posted_date', 'content')

admin.site.register(Posts, PostsAdmin)