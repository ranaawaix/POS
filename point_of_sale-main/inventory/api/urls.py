from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventory.api import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'categories', views.CategoriesAPIViewset, basename='categories')
router.register(r'suppliers', views.SuppliersAPIViewset, basename='suppliers')
router.register(r'expenses', views.ExpenseAPIViewset, basename='expenses')
router.register(r'purchaseorders', views.PurchaseOrderAPIViewset, basename='purchaseorders')
router.register(r'products', views.ProductAPIViewset, basename='products')
router.register(r'producttypes', views.ProductTypeAPIViewset, basename='producttypes')
router.register(r'barcodes', views.BarcodeAPIViewset, basename='barcodes')
# router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]