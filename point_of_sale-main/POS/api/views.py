from rest_framework import viewsets
from POS.api.serializers import StoreSerializer, CustomerSerializer, SaleSerializer
from POS.models import Store, Customer, Sale
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StoreAPIViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CustomerAPIViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class POSAPIViewset(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
