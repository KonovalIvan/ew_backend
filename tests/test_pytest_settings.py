import pytest as pytest
from assertpy import assert_that

from apps.authentication.models import User


# tests for generate same models
@pytest.mark.django_db
def test_first_test():
    user = User.objects.create(
        username='test_user'
    )
    assert User.objects.get(username='test_user').username == user.username


@pytest.mark.django_db
def test_second_test():
    user = User.objects.create(
        username='test_user1'
    )
    assert User.objects.get(username='test_user1').username == user.username


@pytest.mark.django_db
def test_third_test():
    user = User.objects.create(
        username='test_user1'
    )
    assert User.objects.get(username='test_user1').username == user.username


def test_4_test():
    assert_that(User.objects.create).raises(RuntimeError).when_called_with(username='test_user')
