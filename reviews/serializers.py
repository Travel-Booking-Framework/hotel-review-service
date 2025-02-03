from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
    # Custom validation logic
    # Raise serializers.ValidationError if validation fails
        return data