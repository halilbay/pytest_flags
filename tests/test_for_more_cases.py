import pytest
from tortoise.exceptions import ValidationError

from app.models import Book, Order, Customer


@pytest.mark.success
@pytest.mark.parametrize("quantity", [1, 5, 10])
@pytest.mark.asyncio
async def test_create_order_success(quantity):
    """
    Successful order creation with different quantities
    """
    book = await Book.create(title="Test Book", author="Test Author", stock=15)
    customer = await Customer.create(name="Test Customer", email="test@example.com")
    order = await Order.create(book=book, quantity=quantity, customer=customer)
    assert order.quantity == quantity

@pytest.mark.failure
@pytest.mark.parametrize("quantity", [20, 30, 50])
@pytest.mark.asyncio
async def test_create_order_failure(quantity):
    """
    Fail due to ordering more than available stock
    """
    book = await Book.create(title="Test Book", author="Test Author", stock=10)
    customer = await Customer.create(name="Test Customer", email="test@example.com")
    with pytest.raises(ValidationError):
        await Order.create(book=book, customer=customer, quantity=quantity)

# Generate 50 more test cases
@pytest.mark.parametrize("stock, quantity, expected", [
    (10, 5, True),
    (20, 25, False),
    (15, 15, True),
    (0, 1, False),
    pytest.param(50, 45, True, marks=pytest.mark.success),
] * 50)  # Repeat for more cases
@pytest.mark.asyncio
async def test_order_quantity_stock(stock, quantity, expected):
    """
    Test if the order quantity matches the stock or exceeds it
    """
    book = await Book.create(title="Test Book Multiple", author="Author", stock=stock)
    customer = await Customer.create(name="Test Customer", email="test@example.com")
    if expected:
        order = await Order.create(book=book, customer=customer, quantity=quantity)
        assert order.quantity == quantity
    else:
        with pytest.raises(ValidationError):
            await Order.create(book=book, customer=customer, quantity=quantity)
