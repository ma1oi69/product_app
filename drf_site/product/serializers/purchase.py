from rest_framework import serializers

from product.models import Product


class ProductPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'count_lessons', 'start_date', 'price', 'id']

    def info_for_payment(self, validate_data):
        user_id = self.context['request'].user.id
        product_data = {
            'name': validate_data['name'],
            'count_lessons': validate_data['count_lessons'],
            'start_date': validate_data['start_date'],
            'price': validate_data['price'],
            'teacher_id': user_id,
            'products_access_received': [validate_data['id']]
        }
        return product_data
