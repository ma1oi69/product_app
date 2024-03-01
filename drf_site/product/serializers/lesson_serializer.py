from rest_framework import serializers

from product.models import Lesson, Product


class LessonSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Lesson
        fields = ['name', 'video_link', 'product_id']






