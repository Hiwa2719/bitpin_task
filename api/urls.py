from django.urls import path
from .views import RatingView, ArticleView

urlpatterns = [
    path('articles/', ArticleView.as_view(), name='articles-view'),
    path('vote/', RatingView.as_view(), name='vote-view'),
]
