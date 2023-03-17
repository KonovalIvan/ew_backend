import pytest as pytest

from apps.authentication.models import User


@pytest.mark.django_db
def test_first_test():
    user = User.objects.create(username="test_user")
    user.first_name = "Ivan"
    user.last_name = "Konoval"
    user.save()
    user.refresh_from_db()

    assert user.username == "test_user"
    assert user.first_name == "Ivan"
    assert user.last_name == "Konoval"
