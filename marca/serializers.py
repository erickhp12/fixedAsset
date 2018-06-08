from rest_framework import serializers

from marca.models import Marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class singleMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'