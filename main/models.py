from django.db import models
from django.utils import timezone
  
class Quiry(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    msg = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=0,choices=((1,'Resolved'),(0,'Pending')))
    
    def set_quiry_to_resolve(self, request, queryset):
        count = queryset.update(status = True)
        self.message_user(request, '{} Quiry have been Resolved successfully.'.format(count))
    set_quiry_to_resolve.short_description = "Resolved the selected Quiries"
    
    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=40, default='Graphic Designer')
    text = models.CharField(max_length=100, default="There are many variations of passagesn of but the majority have suffered alteration in some form.")
    icon = models.ImageField(upload_to='Service')
    def __str__(self):
        return self.title
class Work(models.Model):
    category = models.CharField(max_length=20, blank=True, default='Web Development')
    link = models.CharField(max_length=200, blank=True, default='#')
    image = models.FileField(upload_to='work')
    def __str__(self):
        return self.category
class AboutMe(models.Model):
    mobile = models.CharField(max_length=15, default='9506693774')
    name = models.CharField(max_length=20, default='Raj Pandey')
    email = models.EmailField()
    insta = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    insta_username = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    whatsapp = models.CharField(max_length=150, blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    cv = models.FileField(upload_to='Resume/')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'About Me'
