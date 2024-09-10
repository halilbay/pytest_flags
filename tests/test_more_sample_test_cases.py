import pytest
from tortoise.exceptions import ValidationError

from app.models import Book


@pytest.mark.success
@pytest.mark.parametrize("title, author, stock", [
    ("Book A", "Author A", 10),
    ("Book B", "Author B", 20),
    ("Book C", "Author C", 5),
])  # Repeat to create more cases
@pytest.mark.asyncio
async def test_create_book_success(title, author, stock):
    """
    Successfully create books with different stock values
    """
    book = await Book.create(title=title, author=author, stock=stock)
    assert book.title == title
    assert book.author == author
    assert book.stock == stock

@pytest.mark.failure
@pytest.mark.parametrize("stock", [-1, -5, -10])
@pytest.mark.asyncio
async def test_create_book_failure(stock):
    """
    Fail to create a book with a negative stock value
    """
    with pytest.raises(ValidationError):
        await Book.create(title="Negative Stock Book", author="Author", stock=stock)

# Additional tests to create more variety
@pytest.mark.parametrize("title, stock", [
    ("Book D", 5),
    ("Book E", 50),
    ("Book F", 100),
] * 50)
@pytest.mark.asyncio
async def test_book_update_stock(title, stock):
    """
    Test updating the stock value of a book
    """
    book = await Book.create(title=title, author="Author", stock=10)
    book.stock = stock
    await book.save()
    assert book.stock == stock
