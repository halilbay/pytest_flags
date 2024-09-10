import asyncio
import time

from tortoise import Tortoise
from tortoise.contrib.test import _init_db, getDBConfig
import pytest

@pytest.fixture(autouse=True)
def initialize_test_db(request, event_loop):
    time.sleep(0.005) # Added only for slow cases
    config = getDBConfig(app_label="models", modules=["app.models"])

    event_loop.run_until_complete(_init_db(config))

    request.addfinalizer(
        lambda: event_loop.run_until_complete(Tortoise._drop_databases())
    )


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()