from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'count_lessons', 'start_date', 'price',
                  'min_students', 'max_students', 'count_groups']

    def create(self, validate_data):
        user_id = self.context['request'].user.id

        product = Product.objects.create(teacher_id=user_id, **validate_data)

        return product

