from django.contrib import admin

from apps.authentication.models import User, Address


class UserAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
