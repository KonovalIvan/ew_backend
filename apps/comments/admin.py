from django.contrib import admin

from apps.comments.models import Comments


class CommentaryAdmin(admin.ModelAdmin):
    model = Comments
    list_display = (
        "short_description",
        "task",
        "updated_at",
    )
    list_filter = ("updated_at",)
    readonly_fields = ("creator",)


admin.site.register(Comments, CommentaryAdmin)
