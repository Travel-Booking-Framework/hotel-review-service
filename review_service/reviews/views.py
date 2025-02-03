from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from .repository import ReviewRepository
from .commands import CreateReviewCommand, DeleteReviewCommand

class CreateReviewView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            command = CreateReviewCommand(serializer.validated_data)
            command.execute()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListReviewsView(APIView):
    def get(self, request, *args, **kwargs):
        hotel_id = request.query_params.get('hotel_id')
        if hotel_id:
            reviews = ReviewRepository.get_reviews_by_hotel(hotel_id)
        else:
            reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class DeleteReviewView(APIView):
    def delete(self, request, *args, **kwargs):
        review_id = kwargs.get('review_id')
        review = ReviewRepository.get_review_by_id(review_id)
        if review:
            command = DeleteReviewCommand(review.id)
            command.execute()
            return Response({'message': 'Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
