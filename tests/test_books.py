import pytest

from app.models import Book


@pytest.mark.asyncio
@pytest.mark.parametrize("title, author, stock", [
    ("The Great Gatsby", "F. Scott Fitzgerald", 5),
    ("1984", "George Orwell", 3),
    pytest.param("Invisible Man", "Ralph Ellison", 2, marks=pytest.mark.success),
])
async def test_create_book_success(title, author, stock):
    book = await Book.create(title=title, author=author, stock=stock)
    assert book.id is not None
    assert book.stock == stock


@pytest.mark.asyncio
async def test_update_book_stock_success():
    await Book.create(title="1984", author="George Orwell", stock=3)
    book = await Book.get(title="1984")
    book.stock += 5
    await book.save()
    updated_book = await Book.get(title="1984")
    assert updated_book.stock == 8


@pytest.mark.asyncio
async def test_create_book_failure():
    with pytest.raises(Exception):
        await Book.create(title=None, author="Unknown Author", stock=5)
