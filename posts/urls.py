from django.urls import path
from .views import PostList, RatesCreateAPIView

urlpatterns = [
    path('', PostList.as_view()),
    path('rate', RatesCreateAPIView.as_view()),
]
