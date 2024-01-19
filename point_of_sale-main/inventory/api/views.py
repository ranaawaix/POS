from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from inventory.api.serializers import CategoriesSerializer, SupplierSerializer, ExpenseSerializer, \
    PurchaseOrderItemSerializer, PurchaseSerializer, ProductSerializer, ProductTypeSerializer, BarcodeSerializer
from inventory.models import Category, PurchaseOrder, PurchaseOrderItem, Supplier, Expense, Product, ProductType, Barcode


class CategoriesAPIViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class SuppliersAPIViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ExpenseAPIViewset(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderItemAPIViewset(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderAPIViewset(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductAPIViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductTypeAPIViewset(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BarcodeAPIViewset(viewsets.ModelViewSet):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer
    # pagination_class = [PageNumberPagination]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
