from __future__ import unicode_literals
from django.utils import timezone as django_tz
from django.db import models
 
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be of valid email format."
        if len(postData['password']) < 8:
            errors['short_password'] = "Password must be 8 characters or more."
        if postData['password'] != postData['conf_password']:
            errors['password_mismatch'] = "Password and password confirmation must match."
        return errors

    def create_user(self, first, last, email, password):
        try:
            return User.objects.create(first_name=first, last_name=last, email=email, password=password)
        except:
            return None

    def login_validator(self, postData):
        errors = {}
        try:
            user = User.objects.get(email=postData['email'])
            if user:
                if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    return user
                else:
                    errors['pass_match'] = "Password does not match our records"
                return errors
        except:
            errors['not_reg'] = "You are not registered"
            return errors     


class User(models.Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name


class Dog(models.Model):
    name = models.CharField(max_length = 255)
    rescue_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length = 255)
    source_note = models.TextField(null=True, blank=True)
    microchip_number = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 10)
    birthdate = models.DateField(null=True, blank=True)
    description = models.CharField(max_length = 255)
    weight = models.IntegerField()
    fixed = models.BooleanField()
    adopted = models.BooleanField(default=False)
    thumb = models.ImageField(blank=True, default="pup8.jpg")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    on_delete=models.CASCADE

    def __str__(self):
        return self.name


class VaccineDog(models.Model):
    vaccine_name = models.CharField(max_length=100)
    vaccine_given = models.DateField(null=True, blank=True)
    vaccine_due = models.DateField()
    vaccine_number = models.CharField(default=None, blank=True, null=True, max_length = 100)
    vaccine_notes = models.TextField(max_length = 500)
    dog = models.ForeignKey(Dog, related_name="vaccines", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vaccine_name

class PreventionDog(models.Model):
    prevention_name = models.CharField(max_length=100)
    prevention_given = models.DateField(null=True, blank=True)
    prevention_due = models.DateField()
    prevention_notes = models.TextField(max_length=500)
    dog = models.ForeignKey(Dog, related_name="preventions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prevention_name

class TestDog(models.Model):
    test_name = models.CharField(max_length=100)
    test_given = models.DateField(null=True, blank=True)
    test_due = models.DateField()
    test_notes = models.TextField(max_length=500)
    dog = models.ForeignKey(Dog, related_name="tests", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.test_name


class Cat(models.Model):
    name = models.CharField(max_length = 255)
    rescue_date = models.DateField()
    source = models.CharField(max_length = 255)
    source_note = models.TextField()
    microchip_number = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 10)
    birthdate = models.DateField()
    description = models.CharField(max_length = 255)
    weight = models.IntegerField()
    fixed = models.BooleanField()
    thumb = models.ImageField(blank=True, default="default_cat.jpg")
    adopted = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    on_delete=models.CASCADE

    def __str__(self):
        return self.name

class VaccineCat(models.Model):
    vaccine_name = models.CharField(max_length=100)
    vaccine_given = models.DateField(null=True, blank=True)
    vaccine_due = models.DateField()
    vaccine_number = models.CharField(default=None, blank=True, null=True, max_length = 100)
    vaccine_notes = models.TextField(max_length = 500)
    cat = models.ForeignKey(Cat, related_name="vaccines", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vaccine_name

class PreventionCat(models.Model):
    prevention_name = models.CharField(max_length=100)
    prevention_given = models.DateField(null=True, blank=True)
    prevention_due = models.DateField()
    prevention_notes = models.TextField(max_length=500)
    cat = models.ForeignKey(Cat, related_name="preventions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prevention_name

class TestCat(models.Model):
    test_name = models.CharField(max_length=100)
    test_given = models.DateField(null=True, blank=True)
    test_due = models.DateField()
    test_notes = models.TextField(max_length=500)
    cat = models.ForeignKey(Cat, related_name="tests", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.test_name
