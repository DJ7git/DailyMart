# In AdminApp/serializers.py
from rest_framework import serializers
from .models import Article  # Adjust if Article is imported elsewhere

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  # Or a specific list of fields
