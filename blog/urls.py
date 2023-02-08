from django.urls import path
from .views import  IndexTemplateView, MenuListView, AboutTemplateView, BookATable

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('book/', BookATable.as_view(), name='book'),
]