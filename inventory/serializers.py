from rest_framework import serializers
class baseserializers(serializers.Serializer):
    name=serializers.CharField(max_length=3)
    quantity=serializers.CharField(max_length=2)