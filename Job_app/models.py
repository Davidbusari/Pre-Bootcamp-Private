from Login_app.models import User
from django.db import models

# Create your models here.

class JobManager(models.Manager):
    def job_validation(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] ="A Title must consist of at least 3 characters"
        if len(postData['desc']) < 3:
            errors['desc'] = "A Decription must consist of at least 3 characters"
        if len(postData['location']) < 3:
            errors['location'] ="A Location must consist of at least 3 characters"
    
        return errors

class Job(models.Model):
    Title = models.CharField(max_length= 255)
    Description = models.TextField()
    Location = models.CharField(max_length=255)
    Categories = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    Posted_by = models.ForeignKey(User, related_name = 'jobs', on_delete= models.CASCADE)
    users_joined = models.ManyToManyField(User, related_name= 'jobs_joined')
    objects = JobManager()