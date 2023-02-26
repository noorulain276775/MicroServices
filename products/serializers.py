from rest_framework import serializers
from .models import AllProducts


class AllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProducts
        fields = "__all__"


