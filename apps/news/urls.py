from django.urls import path
from .views import MainPageView, NewsDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='news_list_url'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail_url'),
    
]