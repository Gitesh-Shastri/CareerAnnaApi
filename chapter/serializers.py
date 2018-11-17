from rest_framework.serializers import ModelSerializer
from .models import chapter_name

class ChapterNameListSerializer(ModelSerializer):

    class Meta:

        model = chapter_name
        fields = '__all__'
        
class ChapterNameCreateSerializer(ModelSerializer):

    class Meta:

        model = chapter_name
        fields = [
            'CATEGORY_ID',	
            'SUB_CATEGORY_ID', 	
            'EXAM_ID',	
            'CHAPTER_NAME',	
            'ACTIVE_STATUS',	
            'CREATED_DATE'
        ]        