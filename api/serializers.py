from rest_framework import serializers
from .models import Article, Rating


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
