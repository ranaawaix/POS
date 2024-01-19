from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_accounts.api import views

# Create a router and register our ViewSets with it.
# router = DefaultRouter()
# router.register(r'createusers', views.CreateUserAPIView.as_view(), basename='createusers'),
# router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('create_user/', views.CreateUserAPIView.as_view(), name='create-user'),
]