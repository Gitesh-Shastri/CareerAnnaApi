from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from .models import chapter_name
from .serializers import (
    ChapterNameCreateSerializer,
    ChapterNameListSerializer
    )
from django.db.models import Q    

# Create your views here.
class ListChapterNameView(generics.ListAPIView):

    queryset = chapter_name.objects.all()
    serializer_class = ChapterNameListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = chapter_name.objects.all()
        query = self.request.GET.get('CATEGORY_ID')
        if query:
            queryset_list = queryset_list.filter(
                Q(CATEGORY_ID__icontains=query)
            )
        return queryset_list

class CreateChapterNameView(generics.CreateAPIView):

    queryset = chapter_name.objects.all()
    serializer_class = ChapterNameCreateSerializer    

