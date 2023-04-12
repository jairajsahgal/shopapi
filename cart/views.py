from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer, UpdateCartItemSerializer


class CartViewset(ModelViewSet):
    """Viewset for Cart model"""

    http_method_names = ["get", "post", "delete"]
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Overriding to return current user to create cart"""
        return {"user": self.request.user}

    def get_queryset(self):
        """Overriding to load only user specific cart"""
        queryset = Cart.objects.prefetch_related("items").filter(user=self.request.user)
        return queryset


class CartItemViewset(ModelViewSet):
    """Viewset for CartItem model"""

    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Overriding to load only cart specific items"""
        items = CartItem.objects.filter(cart=self.kwargs["cart_pk"])
        return items

    def get_serializer_context(self):
        """Overriding to return cart pk for creating cart items"""
        return {"cart_pk": self.kwargs["cart_pk"]}

    def get_serializer_class(self):
        """Return serializer class based on HTTP request method"""
        if self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer
