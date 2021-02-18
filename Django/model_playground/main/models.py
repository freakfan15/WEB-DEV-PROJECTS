from django.core import validators
from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug
)
from main.validators import validate_even_number

# Create your models here.

#every table in a database is represented as a class
#every row in database is represented by a object of this class
class Student(models.Model): #Student class extends a class called Model which is inside models module
    GENDERS =(
        ('f', 'Female'),      #in this GENDER tuple we have a list of tuples. In each tuple the first elemnent shows the 
        ('m', 'Male'),        #value which is actually stored ACTUALLY in the database and second elemnt is what is displayed
        ('u', 'undisclosed')  #on the frontend.
    )
    #varchar(100)
    name = models.CharField(max_length=100)
    #integer
    roll_no = models.IntegerField(unique=True)
    #Text TextField doesnot have size  limitations as CharFiled
    #assigning null means it is allowed null at database level
    #but not allowed to be null at ORM level
    address = models.TextField(null=True)
    
    phone_number = models.CharField(max_length=15, null=True, blank=True) #blank =True means we can leave the field black or null even at ORM LEVEL now
    #varchar(255)
    email = models.CharField(max_length=100,  null=True, validators=[EmailValidator(message="Email not valid")]) #validators accepts a list of all the validators required

    gender = models.CharField(max_length=1, choices=GENDERS, null=True)

    age = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(150),
            MinValueValidator(3),
            validate_even_number
        ]
    )
    #valid “slug” consists of letters, numbers, underscores or hyphens only
    slug = models.CharField(max_length=100, null=True, validators=[validate_slug])

    #To change the look where it writes student object 1. It does not look so good, so we use can use dunders to modify them
    def __str__(self):
        return self.name

     
