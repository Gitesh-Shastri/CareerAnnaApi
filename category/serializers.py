from rest_framework.serializers import ModelSerializer
from .models import ca_category

class CategoryListSerializer(ModelSerializer):

    class Meta:

        model = ca_category
        fields = '__all__'

class CategoryCreateSerializer(ModelSerializer):

    class Meta:

        model = ca_category
        fields = [
            'CATEGORY_NAME',
            'ACTIVE_STATUS',
            'PRIORITY_STATUS',
            'CREATED_DATE',
            'cimage'
        ]       

