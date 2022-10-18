from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Article, Rating
from .serializers import RatingSerializer


class RatingView(CreateAPIView):
    queryset = Rating.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
