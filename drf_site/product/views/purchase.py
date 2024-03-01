import datetime

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.exceptions.exceptions import ProductNotExists
from product.models import Product, UserProduct, UserGroup, Group
from product.serializers.serializers import ProductSerializer
from product.services.user_product import add_access


class ProductBuyAPIView(APIView):
    def post(self, request, product_id):
        try:
            product = get_object_or_404(Product, id=product_id)
        except ProductNotExists:
            return Response({"error": "Product not found"}, status=status.HTTP_403_FORBIDDEN)

        user = request.user

        if user.role == 'teacher':
            return Response({"error": "Product buy not available"}, status=status.HTTP_404_NOT_FOUND)

        card_number = request.data.get('card_number')
        cvc = request.data.get('cvc')
        amount = request.data.get('amount')

        if amount == product.price:
            add_access(product_id, request.user.id)

        user_product = UserProduct.objects.all()
        if user_product.filter(user=user).exists():
            if product.start_date >= datetime.datetime.now():
                Group.objects.filter(product_id=product.id, )
            UserGroup.objects.create(user_id=user, )

            return Response({"message": "Payment successful and access received to 2 product", "product":
                                    ProductSerializer(product).data, "products_access_received": [product_id]},
                                    status=status.HTTP_200_OK)


