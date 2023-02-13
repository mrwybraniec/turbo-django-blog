# Current App
import environ
import pytest
from django.conf import settings


env = environ.Env()

TEMPORARY_DATABASE_LOCATION: str = "sqlite:////tmp/tmp-db.sqlite3"


@pytest.fixture(autouse=True)
def use_dummy_db_location():
    """Swap app database with the dummy one."""
    settings.DATABASES = {"default": env.db_url(default=TEMPORARY_DATABASE_LOCATION)}
