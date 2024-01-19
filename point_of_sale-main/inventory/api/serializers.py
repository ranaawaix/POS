from POS.models import StoreProduct
from inventory.models import Category, PurchaseOrder, PurchaseOrderItem, Expense, Supplier, Product, ProductType, \
    Barcode
from rest_framework import serializers
from inventory.api.services import create_purchase_order, update_purchase_order, create_product, update_product


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name']


class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['name']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image', 'code', 'name']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Category.objects.create(**validated_data)


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['date', 'reference', 'amount', 'attachment', 'note']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Expense.objects.create(**validated_data)


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'supplier_custom_field_1', 'supplier_custom_field_2']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Supplier.objects.create(**validated_data)


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['product', 'quantity', 'price', 'total']


class PurchaseSerializer(serializers.ModelSerializer):
    purchaseorderitems = PurchaseOrderItemSerializer(many=True)
    supplier = serializers.PrimaryKeyRelatedField(many=False, queryset=Supplier.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['date', 'reference', 'purchaseorderitems', 'total', 'supplier', 'status', 'attachment', 'note']

    def create(self, validated_data):
        user = self.context['request'].user
        purchase_order = create_purchase_order(validated_data, user)
        return purchase_order

    def update(self, instance, validated_data):
        user = self.context['request'].user
        purchase_order = update_purchase_order(instance, validated_data, user)
        return purchase_order


class StoreProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProduct
        fields = ['store', 'store_price', 'quantity']


class ProductSerializer(serializers.ModelSerializer):
    storeproducts = StoreProductSerializer(many=True)
    type = serializers.PrimaryKeyRelatedField(many=False, queryset=ProductType.objects.all())
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    barcode_symbology = serializers.PrimaryKeyRelatedField(many=False, queryset=Barcode.objects.all())

    class Meta:
        model = Product
        fields = ['type', 'name', 'code', 'barcode_symbology', 'category', 'cost', 'price', 'product_tax', 'tax_method',
                  'alert_quantity', 'image', 'details', 'storeproducts']

    def create(self, validated_data):
        user = self.context['request'].user
        product = create_product(validated_data, user)
        return product

    def update(self, instance, validated_data):
        user = self.context['request'].user
        product = update_product(instance, validated_data, user)
        return product
