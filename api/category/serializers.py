from django.db.models import fields
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serizalizer):
    class Meta:
        model = Category
        fields = ('name','description')