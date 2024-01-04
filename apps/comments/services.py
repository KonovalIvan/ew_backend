from apps.authentication.models import User
from apps.comments.models import Comments


class CommentsServices:
    @staticmethod
    def add_comment(data: dict, user: User) -> Comments:
        data["creator"] = user
        return Comments.objects.create(**data)
