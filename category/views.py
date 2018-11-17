from rest_framework import generics
from .models import ca_category
from .serializers import (
    CategoryListSerializer,
    CategoryCreateSerializer
    )

# Create your views here.
class ListCategoryView(generics.ListAPIView):

    queryset = ca_category.objects.all()
    serializer_class = CategoryListSerializer

class CreateCategoryView(generics.CreateAPIView):

    queryset = ca_category.objects.all()
    serializer_class = CategoryCreateSerializer