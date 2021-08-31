from django.db import models
from users.models import User
from branches.models import Branch
from menus.models import Menu

# Create your models here.
class Payment(models.Model):
    class Meta:
        db_table = 'payment'
    #
    def __int__(self):
        return self.id

    payment_method = models.CharField(max_length=10)
    payment_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    payment_completion = models.BooleanField()


class Order(models.Model):
    class Meta:
        db_table = 'order'

    def __int__(self):
        return self.id

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    personal_information = models.ForeignKey(User, on_delete=models.CASCADE)
    take_out = models.BooleanField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class OrderMenu(models.Model):
    class Meta:
        db_table = 'order_menu'

    def __int__(self):
        return self.id

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_menu_memo = models.CharField(max_length=255, null=True)
    count = models.IntegerField()
