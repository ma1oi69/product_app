from rest_framework import status
from rest_framework.views import APIView
from product.models import Product, Lesson

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class CreateLessonAPIView(APIView):
    def post(self, request, product_id):
        user = request.user

        if user.role != "teacher":
            return Response({"error": "You are not allowed to create lessons"}, status=status.HTTP_403_FORBIDDEN)

        lessons_data = request.data

        if not lessons_data:
            return Response({"error": "No lesson data provided"}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=product_id)

        created_lessons = []
        for lesson_data in lessons_data:
            name = lesson_data.get('name')
            video_link = lesson_data.get('video_link')
            lesson = Lesson.objects.create(name=name, video_link=video_link, product_id=product_id)
            created_lessons.append(lesson)

        return Response({"success": "Lessons created successfully"}, status=status.HTTP_201_CREATED)



