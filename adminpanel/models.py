# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class CustomerRepository(models.Model):
    
    RowNumber=models.CharField(max_length=100,blank=True)	
    CustomerId=models.CharField(max_length=100,blank=True)
    Surname=models.CharField(max_length=100,blank=True)
    CreditScore=models.CharField(max_length=100,blank=True)
    Geography=models.CharField(max_length=100,blank=True)
    Gender=models.CharField(max_length=100,blank=True)
    Age=models.CharField(max_length=100,blank=True)
    Tenure=models.CharField(max_length=100,blank=True)
    Balance=models.CharField(max_length=100,blank=True)
    NumOfProducts=models.CharField(max_length=100,blank=True)
    HasCrCard=models.CharField(max_length=100,blank=True)
    IsActiveMember=models.CharField(max_length=100,blank=True)
    EstimatedSalary=models.CharField(max_length=100,blank=True)
    Exited=models.CharField(max_length=100,blank=True)
    Complain=models.CharField(max_length=100,blank=True)
    SatisfactionScore=models.CharField(max_length=100,blank=True)
    CardType=models.CharField(max_length=100,blank=True)
    PointEarned=models.CharField(max_length=100,blank=True) 
    Mobile=models.CharField(max_length=100,blank=True)	
    CardNo=models.CharField(max_length=100,blank=True)
    DOB = models.DateField(null=True, blank=True)


class Frequest_query_set(models.Model):
    category = models.CharField(max_length=2000)
    query = models.CharField(max_length=2000)
    
class SearchedEntry(models.Model):
    entry = models.ForeignKey(CustomerRepository, on_delete=models.CASCADE)
    searched_value = models.CharField(max_length=255)
    searched_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
def generate_complain_id():
    # Assuming you want to start with 1 and increment by 1
    last_complaint = complaints_info.objects.order_by('-auto_id').first()
    if last_complaint:
        return last_complaint.auto_id + 1
    return 1


class complaints_info(models.Model):
    complain_id = models.CharField(primary_key=True,max_length=12, unique=True, editable=False)
    auto_id = models.IntegerField(auto_created=True)
    urgency = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    complained_through = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    remarks = models.CharField(max_length=1000,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.complain_id:
            self.auto_id = generate_complain_id()
            self.complain_id = f'TCKT{self.auto_id:08d}'
        super().save(*args, **kwargs)
        
class complain_details(models.Model):
    complain_id=models.ForeignKey(complaints_info, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    query = models.CharField(max_length=100)
    other_query = models.CharField(max_length=1000,blank=True)
    
    def __str__(self):
        return self.complain_id