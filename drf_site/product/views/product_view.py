from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.exceptions.exceptions import CustomUserNotExists

from product.models import Product
from product.serializers.serializers import ProductSerializer
from product.services.user_product import create_group


class ProductAPIView(APIView):

    def get(self, request):
        courses = Product.objects.all()
        serializer = ProductSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        try:
            user = request.user

            if user.role == 'teacher':
                serializer = ProductSerializer(data=request.data, context={'request': request})

                if serializer.is_valid():

                    count_groups = request.data['count_groups']

                    create_group(count_groups=count_groups, product=serializer.save())

                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'No rights'}, status=status.HTTP_403_FORBIDDEN)
        except CustomUserNotExists:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
