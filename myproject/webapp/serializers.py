from dataclasses import fields
from rest_framework import serializers
from webapp.models import employee


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
#        fields=('firstname','lastname')
        fields="__all__"