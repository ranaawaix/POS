from POS.models import Sale, SaleItem, Register, Hold, Payment


def create_sale(user, validated_data):
    validated_data['user'] = user
    saleitems = validated_data.pop('saleitems')
    hold = validated_data.pop('hold') if validated_data.get('hold') else None
    payment = validated_data.pop('payment') if validated_data.get('payment') else None
    sale = Sale.objects.create(**validated_data)
    if hold:
        hold['sale'] = sale
        Hold.objects.create(**hold)
        sale.status = 'H'
        sale.save()
    if payment:
        payment['sale'] = sale
        Payment.objects.create(**payment)
        sale.status = 'P'
        sale.save()
    for item in saleitems:
        item['sale'] = sale
        cash_in_hand = item.pop('register')
        store = cash_in_hand['store']
        opening_cash_in_hand = cash_in_hand['opening_cash_in_hand']
        Register.objects.get_or_create(opening_cash_in_hand=opening_cash_in_hand, store=store, user=user, status='O')
        register = Register.objects.get(opening_cash_in_hand=opening_cash_in_hand, store=store, user=user, status='O')
        item['register'] = register
        SaleItem.objects.create(**item)
    return sale


def update_sale(user, instance, validated_data):
    validated_data['user'] = user
    instance.user = user
    saleitems = validated_data.pop('saleitems')
    hold = validated_data.pop('hold') if validated_data.get('hold') else None
    payment = validated_data.pop('payment') if validated_data.get('payment') else None
    instance.customer = validated_data.get('customer')
    instance.total_items = validated_data.get('total_items')
    instance.total_price = validated_data.get('total_price')
    instance.discount = validated_data.get('discount')
    instance.order_tax = validated_data.get('order_tax')
    instance.total_payable = validated_data.get('total_payable')
    instance.save()
    if hold:
        hold['sale'] = instance
        Hold.objects.update_or_create(**hold)
        instance.status = 'H'
        instance.save()
    if payment:
        payment['sale'] = instance
        hold_status = Hold.objects.filter(sale=instance)
        if hold_status:
            hold_status.delete()
        Payment.objects.update_or_create(**payment)
        instance.status = 'P'
        instance.save()
    for item in saleitems:
        item['sale'] = instance
        cash_in_hand = item.pop('register')
        store = cash_in_hand['store']
        opening_cash_in_hand = cash_in_hand['opening_cash_in_hand']
        Register.objects.get_or_create(opening_cash_in_hand=opening_cash_in_hand, store=store, user=user, status='O')
        register = Register.objects.get(opening_cash_in_hand=opening_cash_in_hand, store=store, user=user, status='O')
        item['register'] = register
        SaleItem.objects.update_or_create(**item)
    return instance