from rest_framework import serializers
from POS.api.services import create_sale, update_sale
from POS.models import Store, Customer, Sale, Payment, Hold, SaleItem, Register
from inventory.models import Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'code', 'logo', 'email', 'phone', 'address', 'city', 'country', 'postal_code',
                  'receipt_header', 'receipt_footer', 'user']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'customer_custom_field_1', 'customer_custom_field_2']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['note', 'amount', 'payment_by', 'payment_note']

    def __init__(self, *args, **kwargs):
        super(PaymentSerializer, self).__init__(*args, **kwargs)
        for field in ['amount', 'payment_by']:
            self.fields[field].required = False


class HoldOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hold
        fields = ['reference_note']

    def __init__(self, *args, **kwargs):
        super(HoldOrderSerializer, self).__init__(*args, **kwargs)
        for field in ['reference_note']:
            self.fields[field].required = False


class CashInHandSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(many=False, queryset=Store.objects.all())
    class Meta:
        model = Register
        fields = ['store', 'opening_cash_in_hand']


class SaleItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=False, queryset=Product.objects.all())
    register = CashInHandSerializer()

    class Meta:
        model = SaleItem
        fields = ['register', 'product', 'price', 'quantity', 'total']


class SaleSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(many=False, queryset=Customer.objects.all())
    saleitems = SaleItemSerializer(many=True)
    hold = HoldOrderSerializer(many=False, required=False)
    payment = PaymentSerializer(many=False, required=False)

    class Meta:
        model = Sale
        fields = ['customer', 'saleitems', 'total_items', 'total_price', 'discount', 'order_tax', 'total_payable', 'hold', 'payment']

    def validate(self, data):
        hold_data = data.get('hold')
        payment_data = data.get('payment')

        if hold_data and payment_data:
            raise serializers.ValidationError("Both hold and payment cannot be submitted simultaneously.")

        if not hold_data and not payment_data:
            raise serializers.ValidationError("Either hold or payment should be submitted.")
        else:
            return data

    def create(self, validated_data):
        user = self.context['request'].user
        sale = create_sale(user, validated_data)
        return sale

    def update(self, instance, validated_data):
        user = self.context['request'].user
        sale = update_sale(user, instance, validated_data)
        return sale
