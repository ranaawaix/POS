from rest_framework import serializers
from POS.models import Store
from user_accounts.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    stores = serializers.PrimaryKeyRelatedField(many=True, queryset=Store.objects.all())

    class Meta:
        model = User
        fields = ['group', 'first_name', 'last_name', 'phone', 'gender', 'email', 'username', 'password1', 'password2',
                  'status', 'stores']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
                        }

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Password don't match")
        return attrs

    def create(self, validated_data):
        stores = validated_data.pop('stores')
        password2 = validated_data.pop('password2')
        password1 = validated_data.pop('password1')
        validated_data['password'] = password1
        user = User.objects.create(**validated_data)
        for store in stores:
            user.stores.add(store)
        return user