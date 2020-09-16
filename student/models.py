from django.db import models

# Create your models here.

TYPE_SELECT = (('0', 'Female'),('1', 'male'),)

class Student(models.Model):
    name = models.CharField(max_length=255,blank=True)
    roll_no = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    marks = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='upload',blank=True)
    password = models.CharField(max_length=255,null=True)
    gender = models.CharField(choices=TYPE_SELECT,max_length=20,default=0)
    course = models.CharField(max_length=20,blank=True)

    class Meta:
        db_table='student'
