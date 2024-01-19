from inventory.models import PurchaseOrder, PurchaseOrderItem, Product
from POS.models import StoreProduct


def create_purchase_order(validated_data, user):
    purchase_order_items = validated_data.pop('purchaseorderitems')
    validated_data['user'] = user
    purchase_order = PurchaseOrder.objects.create(**validated_data)
    for item in purchase_order_items:
        item['purchase_order'] = purchase_order
        PurchaseOrderItem.objects.create(**item)
    return purchase_order


def update_purchase_order(instance, validated_data, user):
    purchase_order_items = validated_data.pop('purchaseorderitems')
    validated_data['user'] = user
    instance.user = user
    instance.note = validated_data.get('note')
    instance.reference = validated_data.get('reference')
    instance.status = validated_data.get('status')
    instance.supplier = validated_data.get('supplier')
    instance.date = validated_data.get('date')
    instance.save()
    for item in purchase_order_items:
        item['purchase_order'] = instance
        PurchaseOrderItem.objects.update(**item)
    return instance


def create_product(validated_data, user):
    storeproducts = validated_data.pop('storeproducts')
    validated_data['user'] = user
    product = Product.objects.create(**validated_data)
    for item in storeproducts:
        item['product'] = product
        StoreProduct.objects.create(**item)
    return product


def update_product(instance, validated_data, user):
    storeproducts = validated_data.pop('storeproducts')
    validated_data['user'] = user
    instance.user = user
    instance.type = validated_data.get('type')
    instance.name = validated_data.get('name')
    instance.code = validated_data.get('code')
    instance.barcode_symbology = validated_data.get('barcode_symbology')
    instance.category = validated_data.get('category')
    instance.cost = validated_data.get('cost')
    instance.price = validated_data.get('price')
    instance.product_tax = validated_data.get('product_tax')
    instance.tax_method = validated_data.get('tax_method')
    instance.alert_quantity = validated_data.get('alert_quantity')
    instance.image = validated_data.get('image')
    instance.details = validated_data.get('details')
    instance.save()
    for item in storeproducts:
        item['product'] = instance
        StoreProduct.objects.update(**item)
    return instance
