from .repository import ReviewRepository

class CreateReviewCommand:
    def __init__(self, data):
        self.data = data

    def execute(self):
        return ReviewRepository.create_review(self.data)

class DeleteReviewCommand:
    def __init__(self, review_id):
        self.review_id = review_id

    def execute(self):
        return ReviewRepository.delete_review(self.review_id)