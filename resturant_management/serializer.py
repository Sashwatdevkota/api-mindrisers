from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


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
