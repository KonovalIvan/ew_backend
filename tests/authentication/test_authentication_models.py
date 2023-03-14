import pytest as pytest

from apps.authentication.models import User


# teraz stwarza w normalnej bazie danych użytkownika i nie usuwa go, trzeba to zmienić.
@pytest.mark.django_db
def test_first_test():
    user = User.objects.create(
        username='test_user'
    )
    assert User.objects.get(username='test_user').username == user.username
