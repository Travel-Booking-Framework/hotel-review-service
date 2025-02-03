import grpc
from concurrent import futures
from generated import review_pb2, review_pb2_grpc
from .repository import ReviewRepository

class ReviewService(review_pb2_grpc.ReviewServiceServicer):
    def GetReviews(self, request, context):
        reviews = ReviewRepository.get_reviews_by_hotel(request.hotel_id)
        response = review_pb2.ReviewList()
        for review in reviews:
            response.reviews.add(
                user_id=review.user_id, 
                hotel_id=review.hotel_id,
                rating=review.rating,
                comment=review.comment
            )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    review_pb2_grpc.add_ReviewServiceServicer_to_server(ReviewService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()