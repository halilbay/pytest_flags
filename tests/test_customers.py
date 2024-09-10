import pytest
from tortoise.contrib.test import initializer, finalizer

from app.models import Customer


@pytest.mark.asyncio
async def test_create_customer_success():
    customer = await Customer.create(name="Alice", email="alice@example.com")
    assert customer.id is not None
    assert customer.email == "alice@example.com"


@pytest.mark.asyncio
async def test_create_customer_duplicate_email_failure():
    await Customer.create(name="Bob", email="bob@example.com")
    with pytest.raises(Exception):
        await Customer.create(name="Alice Duplicate", email="bob@example.com")


@pytest.mark.asyncio
async def test_create_customer_missing_email_failure():
    with pytest.raises(Exception):
        await Customer.create(name="Charlie", email=None)
