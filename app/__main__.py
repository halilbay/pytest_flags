from tortoise import run_async

from app.db import init_db
from app.models import Book, Order


async def main():
    await init_db()
    print("Welcome to the Bookstore Project!")
    print("Run 'make test' or other make commands to execute tests.")
    await Book.create(
        title="Harry Potter",
        author="J.K. Rowling",
        stock=10,
    )
    x = await Book.all()
    y = await Order.all()

    print(10*"*")
    print(x)
    print(y)
    print(10*"*")

if __name__ == "__main__":
    run_async(main())
