from .models import Article, Category
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.ReadOnlyField(source='category.id')
    class Meta:
        model = Article
        fields = ('id', 'title', 'date', 'url', 'category_id')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'url')