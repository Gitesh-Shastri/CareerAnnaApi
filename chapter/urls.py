from django.conf.urls import url
from .views import (
    ListChapterNameView,
    CreateChapterNameView,
    )

urlpatterns = [
    url(r'^$', ListChapterNameView.as_view(), name="chapter-all"),
    url(r'create/$', CreateChapterNameView.as_view(), name='chapter-create'),
]