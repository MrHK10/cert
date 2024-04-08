from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Agile and Scrum', 'Agile and Scrum'),
        ('Big Data', 'Big Data'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Cyber Security', 'Cyber Security'),
        ('DevOps', 'DevOps'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Health and Safety', 'Health and Safety'),
        ('ISO Certification', 'ISO Certification'),
        ('IT Services Management', 'IT Services Management'),
        ('Project Management', 'Project Management'),
        ('Quality Management', 'Quality Management'),
        ('UX And Design Thinking', 'UX And Design Thinking'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    heading1 = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    description1 = models.TextField(blank=True)
    
    delivery_methods = models.ManyToManyField('DeliveryMethod', blank=True)
    know_mores = models.ManyToManyField('KnowMore', blank=True)
    faqs = models.ManyToManyField('FAQ', blank=True)
    certification_steps = models.ManyToManyField('CertificationStep', blank=True)
    resources = models.ManyToManyField('Resource', blank=True)
    certification_overviews = models.ManyToManyField('CertificationOverview', blank=True)
    learning_outcomes = models.ManyToManyField('LearningOutcome', blank=True)
    def __str__(self):
        return self.category
    
    
class LearningOutcome(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
      
class CertificationOverview(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    
  
class DeliveryMethod(models.Model):
    title = models.CharField(max_length=100, blank=True)
    delivery_method = models.CharField(max_length=100, blank=True)
    delivery_method_list = models.TextField(blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    
   

class KnowMore(models.Model):
    title = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
  

class FAQ(models.Model):
    title = models.CharField(max_length=100, blank=True)
    faq_list = models.CharField(max_length=100, blank=True)
    
   

class CertificationStep(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    

class Resource(models.Model):
    title = models.CharField(max_length=255, blank=True)
    img = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(blank=True)
    
    