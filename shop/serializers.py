from django.conf import settings
from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField("get_image")

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "image"]

    def get_image(self, product):
        return settings.BASE_URL_FULL + product.image.url
