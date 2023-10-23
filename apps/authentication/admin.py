from django.contrib import admin

from apps.authentication.models import Address, User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
