import pytest
from tortoise.transactions import in_transaction

from app.models import Book, Customer


@pytest.mark.asyncio
async def test_transaction_success():
    async with in_transaction() as connection:
        await Book.create(title="Transactional Book", author="Test Author", stock=1, using_db=connection)
        await Customer.create(name="Transactional Customer", email="transact@example.com", using_db=connection)

    book = await Book.get(title="Transactional Book")
    customer = await Customer.get(email="transact@example.com")
    assert book is not None
    assert customer is not None


@pytest.mark.asyncio
async def test_transaction_failure():
    with pytest.raises(Exception):
        async with in_transaction() as connection:
            await Book.create(title=None, author="Test Author", stock=1, using_db=connection)
