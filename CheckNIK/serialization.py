from django.db import models
from rest_framework import serializers
from CheckNIK.models import Dukcapilmodel

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Dukcapilmodel
        fields='__all__'
