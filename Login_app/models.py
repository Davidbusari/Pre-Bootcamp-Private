from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validations (self, postData):
        errors = {}        
        if len(postData['fname']) < 2:
            errors['fname'] = 'First Name must be greater than 2 Characters Long'
        if len(postData['lname']) < 3:
            errors['lname'] = 'Last Name must be greater than 3 Characters Long'
        EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!!!'
        if len(postData['pwd']) < 8:
            errors['pwd'] = 'Password must be greater than 8 Characters Long'
        if postData['pwd'] != postData['conpwd']:
            errors['conpwd'] = 'Password dont match!!!'
        return errors
        
    def login_validation(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!!!'
        # if len(postData['email']) < 2:
        #     errors['email'] = 'Email must be greater than 2 Characters Long'
        if len(postData['pwd']) < 8:
            errors['pwd'] = 'Password must be greater than 8 Characters Long'
        return errors
        
        


class User(models.Model):
    First_name = models.CharField(max_length=55)
    Last_name =models.CharField(max_length=55)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length= 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()





