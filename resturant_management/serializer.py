from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def save(self, **kwargs):
        validated_data = self.validated_data
        item = Category.objects.filter(name=validated_data.get("name")).count()
        if item > 0:
            raise serializers.ValidationError()
        return super().save(self.instance, **kwargs)

    # def create(self, validated_data):
    #     item = Category.objects.filter(name=validated_data.get("name")).count()
    #     if item > 0:
    #         raise serializers.ValidationError({"message": "Data already exists"})
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     item = Category.objects.filter(name=validated_data.get("name")).count()
    #     if item > 0:
    #         raise serializers.ValidationError({"message": "Data already exists"})
    #     return super().update(instance, validated_data)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(name=validated_data.get("name"))

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance


class TableModelSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    num = serializers.CharField()
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        return Table.objects.create(
            num=validated_data.get("num"),
            is_available=validated_data.get("is_available"),
        )

    def update(self, instance, validated_data):
        instance.num = validated_data.get("num", instance.num)

        instance.is_available = validated_data.get(
            "is_available", instance.is_available
        )

        instance.save()

        return instance


class MenuSerializer(ModelSerializer):

    price_with_tax = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            "id",
            "name",
            "category",
            "price",
            "price_with_tax",
            "price_with_discount", 
        ]

    def get_price_with_tax(self, menu: Meta.model):
        return menu.price * 0.13 + menu.price

    def get_price_with_discount(self, menu: Meta.model):
        return self.get_price_with_tax(menu) * 0.9
