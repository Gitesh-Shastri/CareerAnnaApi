from django.conf.urls import url
from .views import (
    ListCategoryView,
    CreateCategoryView
    )

urlpatterns = [ 
    url(r'^$', ListCategoryView.as_view(), name='category-all'),
    url(r'create/$', CreateCategoryView.as_view(), name='category-create')
]
