from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('users/', views.getUsers, name='get_users'),
    # path('users/create_user/', views.createUser, name='create_user'),
    path('workspaces/', views.getWorkspace, name='get_workSpace'),
    path('workspaces/create_workspace', views.createWorkspace, name = 'create_workspace'),
    path('columns/', views.getColumns, name= 'get_columns'),
    path('columns/create_column', views.createColumn, name = 'create_column'),
    path('cards/', views.getCards, name='get_cards'),
    path('cards/create_card', views.createCard, name = 'create_card'),
    path('register/', regiterAPIView.as_view(), name='register'),
    path('login/', loginAPIView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', logoutAPIView.as_view(), name='logout')
]