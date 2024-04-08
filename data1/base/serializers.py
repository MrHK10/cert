from rest_framework import serializers
from .models import Course, LearningOutcome, CertificationOverview, DeliveryMethod, KnowMore, FAQ, CertificationStep, Resource

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LearningOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningOutcome
        fields = '__all__'

class CertificationOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationOverview
        fields = '__all__'

class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = '__all__'

class KnowMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowMore
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class CertificationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationStep
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
