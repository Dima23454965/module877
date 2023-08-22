from django.urls import path
from .views import index, page1, top_sellers


urlpatterns = [
    path('', index),
    path('page1/', page1),
    path('top-sellers/', top_sellers)
]