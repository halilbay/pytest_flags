import os

from tortoise import Tortoise, run_async


async def init_db():
    db_url = os.environ.get("DATABASE_URL", "sqlite://:memory:")
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.models"]}
    )
    await Tortoise.generate_schemas(safe=True)


async def close_db():
    await Tortoise.close_connections()


def init_db_sync():
    run_async(init_db())
