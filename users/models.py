from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'personal_information'

    def __str__(self):
        return self.phone

    age = models.IntegerField()
    sex = models.BooleanField(verbose_name='male') #male=1, female=0
    phone = models.CharField(max_length=11)
    pin = models.CharField(max_length=4)
