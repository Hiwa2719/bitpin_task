from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Article, Rating
from .serializers import RatingSerializer, ArticleSerializer


class ArticleView(APIView):
    """get backs list of all articles"""

    permission_classes = IsAuthenticated,
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True, initial={'user': request.user})
        return Response(serializer.data)


class RatingView(CreateAPIView):
    """updates or creates new rating"""

    queryset = Rating.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
