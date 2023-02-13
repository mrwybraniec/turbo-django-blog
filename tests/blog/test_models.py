# Standard Library
import datetime
import pytest

from django.contrib.auth.models import User

# Current App
from blog.models import Post


@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("_test_user", ["turbo_super_user", "turbo_user"])
def test_post_content(_test_user: str, request: pytest.FixtureRequest):
    # Load fixture from name provided by parametrization
    test_user: User = request.getfixturevalue(_test_user)

    new_post = Post.objects.create(
        author=test_user,
        title="Test Title",
        text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.""",
    )

    test_post = Post.objects.get(id=new_post.id)

    assert test_post.author.username == test_user.username
    assert str(test_post) == "Test Title"
    assert (
        test_post.text
        == """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum."""
    )
    assert isinstance(test_post.created_date, datetime.datetime)
    assert test_post.published_date is None


@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("_test_user", ["turbo_super_user", "turbo_user"])
def test_post_publish_date(_test_user: str, request: pytest.FixtureRequest):
    # Load fixture from name provided by parametrization
    test_user: User = request.getfixturevalue(_test_user)

    new_post = Post.objects.create(
        author=test_user,
        title="Test Title",
        text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.""",
    )

    test_post = Post.objects.get(id=new_post.id)
    test_post.publish()

    assert isinstance(test_post.published_date, datetime.datetime)
