from django.urls import path, include
from rest_framework.routers import DefaultRouter

from POS.api import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'stores', views.StoreAPIViewset, basename='stores'),
router.register(r'customers', views.CustomerAPIViewset, basename='customers'),
router.register(r'sales', views.POSAPIViewset, basename='sales'),


urlpatterns = [
    path('', include(router.urls)),
]
