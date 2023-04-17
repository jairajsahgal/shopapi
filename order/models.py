from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from customer.models import Address
from product.models import Product


class Order(models.Model):
    """
    A model to represent an order placed by a user

    Attributes:
        user (User): user who placed the order
        billing_address(Address): user address that is where bill sent
        shipping_address(Address): user address that is where order is shipped
        created_at (datetime): date and time when the order was created
        updated_at (datetime): date and time when the order was last updated
        delivery (char): status of the order delivery, can be one of:
            - "P" (pending)
            - "C" (complete)
            - "F" (failed)
    """

    DELIVERY_PENDING = "P"
    DELIVERY_COMPLETE = "C"
    DELIVERY_FAILED = "F"

    DELIVERY_CHOICES = [
        (DELIVERY_PENDING, "Pending"),
        (DELIVERY_COMPLETE, "Complete"),
        (DELIVERY_FAILED, "Failed"),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    billing_address = models.ForeignKey(
        Address, on_delete=models.PROTECT, related_name="billing_order"
    )
    shipping_address = models.ForeignKey(
        Address, on_delete=models.PROTECT, related_name="shipping_order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery = models.CharField(
        max_length=1, choices=DELIVERY_CHOICES, default=DELIVERY_PENDING
    )

    def total_price(self):
        """Return total order price"""
        return sum([item.quantity * item.product.price for item in self.items.all()])

    def __str__(self) -> str:
        return str(self.user) + str(self.created_at)


class OrderItem(models.Model):
    """
    A model to represent an item in an order

    Attributes:
        order (Order): order this item belongs to
        product (Product): product being ordered
        ordered_price (decimal): price of the product when it was ordered
        quantity (int): quantity of the product being ordered
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orders",
        help_text="Select an product to order",
    )
    ordered_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Enter the product quantity",
    )

    def total_price(self):
        """Return order item total price"""
        return self.ordered_price * self.quantity

    def __str__(self) -> str:
        return str(self.order)
