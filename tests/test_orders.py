import time

import pytest
from tortoise.contrib.test import initializer, finalizer

from app.models import Order, Customer, Book


@pytest.mark.asyncio
@pytest.mark.success
@pytest.mark.slow
async def test_create_order_success():
    time.sleep(1)
    customer = await Customer.create(name="John Doe", email="john.doe@example.com")
    book = await Book.create(title="The Catcher in the Rye", author="J.D. Salinger", stock=10)
    order = await Order.create(customer=customer, book=book, quantity=1)
    
    assert order.id is not None
    assert order.quantity == 1
    assert order.book.title == "The Catcher in the Rye"


@pytest.mark.asyncio
@pytest.mark.parametrize("quantity, expected", [
    (1, True),
    (15, False),  # More than stock available, should fail
])
async def test_order_quantity_check_success_failure(quantity, expected):
    customer = await Customer.create(name="John Doe", email="john.doe@example.com")
    book = await Book.create(title="The Catcher in the Rye", author="J.D. Salinger", stock=10)

    if expected:
        order = await Order.create(customer=customer, book=book, quantity=quantity)
        assert order.id is not None
    else:
        with pytest.raises(Exception):
            await Order.create(customer=customer, book=book, quantity=quantity)
