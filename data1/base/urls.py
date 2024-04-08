from django.urls import path
from .views import *

urlpatterns = [
    # URLs for Course model
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),

    # URLs for DeliveryMethod model
    path('delivery_methods/', DeliveryMethodListCreateAPIView.as_view(), name='delivery-method-list'),
    path('delivery_methods/<int:pk>/', DeliveryMethodRetrieveUpdateDestroyAPIView.as_view(), name='delivery-method-detail'),

    # URLs for KnowMore model
    path('know_mores/', KnowMoreListCreateAPIView.as_view(), name='know-more-list'),
    path('know_mores/<int:pk>/', KnowMoreRetrieveUpdateDestroyAPIView.as_view(), name='know-more-detail'),

    # URLs for FAQ model
    path('faqs/', FAQListCreateAPIView.as_view(), name='faq-list'),
    path('faqs/<int:pk>/', FAQRetrieveUpdateDestroyAPIView.as_view(), name='faq-detail'),

    # URLs for CertificationStep model
    path('certification_steps/', CertificationStepListCreateAPIView.as_view(), name='certification-step-list'),
    path('certification_steps/<int:pk>/', CertificationStepRetrieveUpdateDestroyAPIView.as_view(), name='certification-step-detail'),

    # URLs for Resource model
    path('resources/', ResourceListCreateAPIView.as_view(), name='resource-list'),
    path('resources/<int:pk>/', ResourceRetrieveUpdateDestroyAPIView.as_view(), name='resource-detail'),

    # URLs for CertificationOverview model
    path('certification_overviews/', CertificationOverviewListCreateAPIView.as_view(), name='certification-overview-list'),
    path('certification_overviews/<int:pk>/', CertificationOverviewRetrieveUpdateDestroyAPIView.as_view(), name='certification-overview-detail'),

    # URLs for LearningOutcome model
    path('learning_outcomes/', LearningOutcomeListCreateAPIView.as_view(), name='learning-outcome-list'),
    path('learning_outcomes/<int:pk>/', LearningOutcomeRetrieveUpdateDestroyAPIView.as_view(), name='learning-outcome-detail'),
]
