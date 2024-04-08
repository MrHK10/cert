from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course, DeliveryMethod, KnowMore, FAQ, CertificationStep, Resource, CertificationOverview, LearningOutcome
from .serializers import CourseSerializer, DeliveryMethodSerializer, KnowMoreSerializer, FAQSerializer, CertificationStepSerializer, ResourceSerializer, CertificationOverviewSerializer, LearningOutcomeSerializer

from django.shortcuts import render
from django.http import JsonResponse
from .models import Course




class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DeliveryMethodListCreateAPIView(ListCreateAPIView):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer

class DeliveryMethodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer

class KnowMoreListCreateAPIView(ListCreateAPIView):
    queryset = KnowMore.objects.all()
    serializer_class = KnowMoreSerializer

class KnowMoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = KnowMore.objects.all()
    serializer_class = KnowMoreSerializer

class FAQListCreateAPIView(ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class CertificationStepListCreateAPIView(ListCreateAPIView):
    queryset = CertificationStep.objects.all()
    serializer_class = CertificationStepSerializer

class CertificationStepRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CertificationStep.objects.all()
    serializer_class = CertificationStepSerializer

class ResourceListCreateAPIView(ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class CertificationOverviewListCreateAPIView(ListCreateAPIView):
    queryset = CertificationOverview.objects.all()
    serializer_class = CertificationOverviewSerializer

class CertificationOverviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CertificationOverview.objects.all()
    serializer_class = CertificationOverviewSerializer

class LearningOutcomeListCreateAPIView(ListCreateAPIView):
    queryset = LearningOutcome.objects.all()
    serializer_class = LearningOutcomeSerializer

class LearningOutcomeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LearningOutcome.objects.all()
    serializer_class = LearningOutcomeSerializer
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Course

# def course_list(request):
#     courses = Course.objects.all()
#     course_data = []
#     for course in courses:
#         course_data.append({
#             'category': course.category,
#             'heading1': course.heading1,
#             'title': course.title,
#             'description1': course.description1,
#             'delivery_methods': [method.title for method in course.delivery_methods.all()],
#             'know_mores': [know_more.title for know_more in course.know_mores.all()],
#             'faqs': [faq.title for faq in course.faqs.all()],
#             'certification_steps': [step.title for step in course.certification_steps.all()],
#             'resources': [resource.title for resource in course.resources.all()],
#             'certification_overviews': [overview.title for overview in course.certification_overviews.all()],
#             'learning_outcomes': [outcome.title for outcome in course.learning_outcomes.all()],
#         })
#     return JsonResponse({'courses': course_data})

# def course_list(request):
#     courses = Course.objects.all()
#     course_data = []
#     for course in courses:
#         course_data.append({
#             'category': course.category,
#             'heading1': course.heading1,
#             'title': course.title,
#             'description1': course.description1,
#             'delivery_methods': [method.title for method in course.delivery_methods.all()],
#             'know_mores': [know_more.title for know_more in course.know_mores.all()],
#             'faqs': [faq.title for faq in course.faqs.all()],
#             'certification_steps': [step.title for step in course.certification_steps.all()],
#             'resources': [resource.title for resource in course.resources.all()],
#             'certification_overviews': [overview.title for overview in course.certification_overviews.all()],
#             'learning_outcomes': [outcome.title for outcome in course.learning_outcomes.all()],
#         })
#     return JsonResponse({'courses': course_data})