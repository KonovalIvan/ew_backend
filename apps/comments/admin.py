from django.contrib import admin

from apps.comments.models import Commentary


class CommentaryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Commentary, CommentaryAdmin)
