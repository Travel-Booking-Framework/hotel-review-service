from djongo import models

class Review(models.Model):
    user_id = models.CharField(max_length=255)
    hotel_id = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['hotel_id']),
            models.Index(fields=['user_id'])
        ]