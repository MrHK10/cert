from django.contrib import admin

from django.contrib import admin
from .models import Course, CertificationOverview ,DeliveryMethod, KnowMore, FAQ, CertificationStep, Resource,LearningOutcome

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('delivery_methods', 'know_mores', 'faqs', 'certification_steps', 'resources','certification_overviews','learning_outcomes')

admin.site.register(DeliveryMethod)
admin.site.register(KnowMore)
admin.site.register(FAQ)
admin.site.register(CertificationStep)
admin.site.register(Resource)
admin.site.register(CertificationOverview)
admin.site.register(LearningOutcome)