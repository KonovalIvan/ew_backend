from django.urls import path

from apps.api.comments.view import AddCommentView

urlpatterns = [
    path("create/", AddCommentView.as_view(), name="new-dashboard"),
]
