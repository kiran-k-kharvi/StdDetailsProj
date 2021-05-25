from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class student_Info(models.Model):
    # MEDIA_CHOICES = [('Audio', (('vinyl', 'Vinyl'),('cd', 'CD'),)),('Video', (('vhs', 'VHS Tape'),('dvd', 'DVD'),)),('unknown', 'Unknown'),]
    ID = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=20,db_column='First Name')
    Last_Name = models.CharField(max_length=20,db_column='Last Name')
    # my_choice = models.CharField(max_length=10,choices=MEDIA_CHOICES)
    Email = models.EmailField()
    Password = models.CharField(max_length=250,db_column='password')
    class Meta:
        verbose_name_plural = "Student Information"
    # MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    # mychoice = models.CharField(max_length=20,choices=MedalType.choices)
    def __str__(self):
        return self.First_Name+" "+self.Last_Name


class portfolio(models.Model):
    student = models.OneToOneField(student_Info,on_delete=CASCADE)
    gitLink = models.URLField(verbose_name="GitHub Link",blank=True)
    profile_pic = models.ImageField(upload_to='profilePic')
    class Meta:
        verbose_name_plural = "Portfolio Details"
    def __str__(self):
        return str(self.student.ID)+" "+self.student.First_Name+" "+ self.student.Last_Name

    