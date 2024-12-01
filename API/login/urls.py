from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.RegisrerView.as_view(), name='login'),
    path('register/', views.RegisrerView.as_view(), name='register'),
]