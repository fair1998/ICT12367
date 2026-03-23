from django.urls import path
from services import views
urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('feedback', views.feedback ),
]