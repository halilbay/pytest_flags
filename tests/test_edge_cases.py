import time

import pytest

from app.models import Book


@pytest.mark.asyncio
async def test_book_edge_case_negative_stock_failure():
    with pytest.raises(Exception):
        await Book.create(title="Negative Stock Book", author="No Author", stock=-5)


@pytest.mark.asyncio
async def test_book_edge_case_large_quantity_success():
    book = await Book.create(title="Large Quantity Book", author="Many Authors", stock=1_000_000)
    assert book.stock == 1_000_000


@pytest.mark.asyncio
@pytest.mark.success
@pytest.mark.slow
async def test_book_edge_case_special_characters_success():
    time.sleep(1)
    book = await Book.create(title="Special & Char@cters!", author="Unusual #Author", stock=10)
    assert book.title == "Special & Char@cters!"
