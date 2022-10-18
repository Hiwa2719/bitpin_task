from rest_framework import serializers
from .models import Article, Rating
from django.db.models import Count, Avg


class ArticleSerializer(serializers.ModelSerializer):
    rating_stat = serializers.SerializerMethodField()
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = 'title', 'rating_stat', 'user_rating'

    def get_user_rating(self, obj):
        user = self.initial.get('user')
        queryset = obj.rating_set.filter(user=user)
        if queryset.exists():
            rating = queryset.first()
            return rating.rating

    def get_rating_stat(self, obj):
        queryset = obj.rating_set.all()
        return queryset.aggregate(rating_count=Count('id'), rating_avg=Avg('rating'))


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = 'user',

    def save(self, **kwargs):
        user = kwargs.get('user')
        article_id = self.validated_data.get('article')
        try:
            obj = Rating.objects.get(user=user, article=article_id)
            obj.rating = self.validated_data.get('rating')
            obj.save()
        except Rating.DoesNotExist:
            obj = Rating.objects.create(user=user, **self.validated_data)
        return obj
