from django.urls import path
from .views import RatingView

urlpatterns = [
    path('vote/', RatingView.as_view()),
]
