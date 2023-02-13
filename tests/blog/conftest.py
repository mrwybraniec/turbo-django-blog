import pytest

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


@pytest.fixture(name="turbo_super_user")
def super_user_fixture(*args, **kwargs) -> User:
    """Fixture returning superuser for the application.

    Returns:
        User: superuser object
    """
    superuser_email = "TurboBlogSU@django.com"
    superuser_username = "turbo_blog_superuser"
    superuser = get_user_model().objects.create_superuser(
        superuser_username, superuser_email
    )
    yield superuser


@pytest.fixture(name="turbo_user")
def turbo_user_fixture(*args, **kwargs) -> User:
    """Fixture returning user for the app.

    Returns:
        User: user object
    """
    user_email = "TurboBlogUser@django.com"
    user_username = "turbo_blog_user"
    user = get_user_model().objects.create_superuser(user_username, user_email)
    yield user
