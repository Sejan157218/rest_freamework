from rest_framework import serializers


class StudentSerializers(serializers.Serializer):
    id=serializers.ImageField();
    name=serializers.CharField(max_length=20);
    roll=serializers.IntegerField();
    city= serializers.CharField(max_length=50)