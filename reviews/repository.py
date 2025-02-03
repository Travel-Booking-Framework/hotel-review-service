from .models import Review

class ReviewRepository:
    @staticmethod
    def create_review(data):
        return Review.objects.create(**data)
    
    @staticmethod
    def get_reviews_by_hotel(hotel_id):
        return Review.objects.filter(hotel_id=hotel_id)
    
    @staticmethod
    def get_review_by_id(review_id):
        return Review.objects.filter(id=review_id).first()
    
    @staticmethod
    def delete_review(review_id):
        return Review.objects.filter(id=review_id).delete()