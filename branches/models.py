from django.db import models


# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    open_time = models.CharField(max_length=5, null=True, blank=True)
    close_time = models.CharField(max_length=5, null=True, blank=True)
    business_license_number = models.CharField(max_length=10)

    class Meta:
        db_table = 'branch'
    def __str__(self):
        return self.branch_name