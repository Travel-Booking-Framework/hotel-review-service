from django.urls import path
from .views import CreateReviewView, ListReviewsView, DeleteReviewView

urlpatterns = [
    path('reviews/', CreateReviewView.as_view(), name='create-review'),
    path('reviews/list/', ListReviewsView.as_view(), name='list-reviews'),
    path('reviews/<int:review_id>/delete/', DeleteReviewView.as_view(), name='delete-review'),
]