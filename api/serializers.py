from rest_framework import serializers
from api.models import *
class SchoolModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'