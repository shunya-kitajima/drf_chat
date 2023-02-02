from django.contrib import admin
from .models import Friends


class FriendAdmin(admin, Friends):
    list_display = ("pk", "user", "friend")


admin.site.register(Friends, FriendAdmin)
