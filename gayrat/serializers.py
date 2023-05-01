from rest_framework import serializers

from gayrat.models import Product, ProductShots, Category


class ProductShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Product1Serializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    shots = ProductShotsSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, validated_data):
        # before
        validated_data = super().to_representation(validated_data)
        # after
        validated_data["gayrat"] = "Kuchemala"
        return validated_data