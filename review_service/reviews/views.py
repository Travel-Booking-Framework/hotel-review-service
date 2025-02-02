from rest_framework import generics
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from .repository import ReviewRepository
from .commands import CreateReviewCommand, DeleteReviewCommand

class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        command = CreateReviewCommand(serializer.validated_data)
        command.execute()

class ListReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        hotel_id = self.request.query_params.get('hotel_id')
        if hotel_id:
            return ReviewRepository.get_reviews_by_hotel(hotel_id)
        return Review.objects.all()

class DeleteReviewView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'review_id'

    def delete(self, request, *args, **kwargs):
        review_id = kwargs.get('review_id')
        command = DeleteReviewCommand(review_id)
        command.execute()
        return Response({'message': 'Review deleted successfully'})