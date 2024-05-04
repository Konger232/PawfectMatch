from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Now

# Supported areas
AREAS = [('BANGKOK', 'Bangkok'), ('NONTHABURI', 'Nonthaburi'), ('PHUKET', 'Phuket'),('PATTAYA', 'Pattaya')]


class Organization(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.CharField(max_length=500, null=True, blank=True)
    area = models.CharField(max_length=100, choices=AREAS, null=True, blank=False)

    def __str__(self):
        return f'{self.name}'
    

class User(AbstractUser):
    
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE, related_name='staff')
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=100, choices=AREAS, null=True, blank=False)
    country = models.CharField(max_length=255, default='Thailand', blank=False)


class Pet(models.Model):

    CHOICES = [('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')]
    LEVELS = [('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('UNKNOWN', 'Unknown')]
    PROGRESS = [('YES', 'Yes'), ('INPROGRESS', 'In Progress'), ('UNKNOWN', 'Unknown')]
    GENDER = [('FEMALE', 'Female'),('MALE', 'Male')]
    ANIMALS = [('DOG', 'Dog'), ('CAT', 'Cat')]
    SIZES = [
        ('S', 'Small (1-10kg)'),
        ('M', 'Medium (11-26kg)'),
        ('L', 'Large (27-45kg)'),
        ('EX', 'Extra Large (46+kg)')
    ]
    AGES = [
        ('PUPPY', 'Puppy'),
        ('YOUNG', 'Young'),
        ('ADULT', 'Adult'),
        ('SENIOR', 'Senior')
    ]

    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=255, choices=ANIMALS, default='DOG', blank=False)
    breed = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, null=True, blank=False)
    age = models.CharField(max_length=20, choices=AGES, null=True, blank=False)
    size = models.CharField(max_length=50, choices=SIZES, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=False)

    registered_date = models.DateField(auto_now_add=True, null=True)
    registered_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='registered_pets')
    adopted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='adopt_pets')
    fostered_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='fostered_pets')
 
    energy = models.CharField(max_length=10, choices=LEVELS, null=True, blank=True)
    anxiety = models.CharField(max_length=10, choices=LEVELS, null=True, blank=True)

    sterilized = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    vaccinated = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)

    images = models.CharField(max_length=500, null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")

    dog_friendly = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    cat_friendly = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    kid_friendly = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)

    house_trained = models.CharField(max_length=10, choices=PROGRESS, null=True, blank=True)
    leash_trained = models.CharField(max_length=10, choices=PROGRESS, null=True, blank=True)
    crate_trained = models.CharField(max_length=10, choices=PROGRESS, null=True, blank=True)

    class Meta:
        ordering = ['-registered_date']
    def __str__(self):
        return f'{self.name}'
    
    def get_total_likes(self):
        return self.likes.count()
    
    
             
class Comment(models.Model):
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(auto_now=True)
    pet = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.commenter}, {self.content}'

