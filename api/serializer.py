from rest_framework import serializers
from api.models import Student


class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=20);
    id=serializers.IntegerField();
    roll=serializers.IntegerField();
    city= serializers.CharField(max_length=50)
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)



# class StudentSerializers_create(serializers.Serializer):
#     name=serializers.CharField(max_length=20);
#     id=serializers.IntegerField();
#     roll=serializers.IntegerField();
#     city= serializers.CharField(max_length=50)

#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)