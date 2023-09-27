from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    days = models.IntegerField()
    syllabus1 = models.TextField(null = True, blank = True)
    syllabus2 = models.TextField(null = True, blank = True)
    syllabus3 = models.TextField(null = True, blank = True)
    syllabus4 = models.TextField(null = True, blank = True)
    syllabus5 = models.TextField(null = True, blank = True)
    syllabus6 = models.TextField(null = True, blank = True)
    syllabus7 = models.TextField(null = True, blank = True)
    syllabus8 = models.TextField(null = True, blank = True)
    syllabus9 = models.TextField(null = True, blank = True)
    syllabus10 = models.TextField(null = True, blank = True)
    syllabus11 = models.TextField(null = True, blank = True)
    syllabus12 = models.TextField(null = True, blank = True)
    syllabus13 = models.TextField(null = True, blank = True)
    syllabus14 = models.TextField(null = True, blank = True)
    syllabus15 = models.TextField(null = True, blank = True)
    syllabus16 = models.TextField(null = True, blank = True)
    syllabus17 = models.TextField(null = True, blank = True)
    syllabus18 = models.TextField(null = True, blank = True)
    syllabus19 = models.TextField(null = True, blank = True)
    syllabus20 = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length = 200)
    message1 = models.TextField(null = True, blank = True)
    message2 = models.TextField(null = True, blank = True)
    message3 = models.TextField(null = True, blank = True)
    message4 = models.TextField(null = True, blank = True)
    message5 = models.TextField(null = True, blank = True)
    message6 = models.TextField(null = True, blank = True)
    message7 = models.TextField(null = True, blank = True)
    message8 = models.TextField(null = True, blank = True)
    message9 = models.TextField(null = True, blank = True)
    message10 = models.TextField(null = True, blank = True)
    message11 = models.TextField(null = True, blank = True)
    message12 = models.TextField(null = True, blank = True)
    message13 = models.TextField(null = True, blank = True)
    message14 = models.TextField(null = True, blank = True)
    message15 = models.TextField(null = True, blank = True)
    message16 = models.TextField(null = True, blank = True)
    message17 = models.TextField(null = True, blank = True)
    message18 = models.TextField(null = True, blank = True)
    message19 = models.TextField(null = True, blank = True)
    message110 = models.TextField(null = True, blank = True)
    
    pictures = models.ImageField(upload_to = 'images', null = True, blank = True)
    def __str__(self):
        return self.name

    
class Team(models.Model):
    name = models.CharField(max_length = 200)
    expertise = models.CharField(max_length = 50)
    experience = models.IntegerField()
    pictures = models.ImageField(upload_to = 'images', null = True, blank = True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 254, null = True, blank = True)
    mobile_number = models.IntegerField(null = True, blank = True)
    college_name = models.CharField(max_length =100, null = True, blank = True)
    message = models.TextField()
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    def __str__(self):
        return self.name