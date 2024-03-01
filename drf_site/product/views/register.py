from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Teachers
from product.serializers.user_serializer import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            password = serializer.validated_data['password']
            confirm_password = request.data.get('confirm_password')

            if password != confirm_password:
                return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()

            if user.role == 'teacher':
                Teachers.objects.create(name=user.username, id=user.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
