from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinValueValidator
from tortoise.exceptions import ValidationError


class Book(Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    published_date = fields.DateField(null=True)
    stock = fields.IntField(default=0, validators=[MinValueValidator(0)])  # stock = fields.IntField() # TODO manipulate for checking --lf or --ff
    


class Customer(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)


class Order(Model):
    id = fields.IntField(primary_key=True)
    customer = fields.ForeignKeyField("models.Customer", related_name="orders")
    book = fields.ForeignKeyField("models.Book", related_name="orders")
    quantity = fields.IntField(validators=[MinValueValidator(1)])

    async def save(self, *args, **kwargs):
        # Fetch the associated book
        book = await Book.get(id=self.book.id)

        
        # Check if the order quantity is greater than the available stock
        if self.quantity > book.stock:
            raise ValidationError(f"Cannot order {self.quantity} items. Only {book.stock} in stock.")

        # If the check passes, proceed with saving the order
        await super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} for {self.quantity} of {self.book.title}"