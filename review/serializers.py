from rest_framework import serializers

from .models import Review, ReviewComment, TemporaryReview

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'

class TemporaryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryReview
        fields = '__all__'