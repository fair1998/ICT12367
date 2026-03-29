from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('form/', views.form),
    path('form/<int:id>/', views.form),
    path('about/', views.about),
    path('delete/<int:id>/', views.delete)
]