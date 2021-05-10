from django.db import models
import datetime
# Create your models here.
class PersonalData(models.Model):
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length=200)
    profession = models.CharField(max_length = 200) 
    about_me = models.CharField(max_length = 510)
    created_at = models.DateField('date created')
    upated_at = models.DateField('date updated')

    def __str__(self):
        return self.about_me
class Projects(models.Model):
    pesonal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    about_project = models.CharField(max_length= 500)


