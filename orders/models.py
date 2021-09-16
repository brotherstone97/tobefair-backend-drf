from django.db import models
from users.models import User
from branches.models import Branch
from menus.models import Menu


# Create your models here.
class Payment(models.Model):
    class Meta:
        db_table = 'payment'

    #ex) 1(2021-08-31)
    def __str__(self):
        return str(self.id) + f'({str(self.payment_date.date())})'

    payment_method = models.CharField(max_length=10)
    payment_date = models.DateTimeField(auto_now_add=True)
    #total_amount자동 계산 필요
    total_amount = models.IntegerField()
    payment_completion = models.BooleanField()


class Order(models.Model):
    class Meta:
        db_table = 'order'

    #ex) 1(1호점)
    def __str__(self):
        return str(self.id) + f'({str(self.branch)})'

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    personal_information = models.ForeignKey(User, on_delete=models.CASCADE)
    take_out = models.BooleanField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class OrderMenu(models.Model):
    class Meta:
        db_table = 'order_menu'

    #2021-08-31 (1(1호점)) 01062557191 
    #년월일 -> 년월일시로 바꿀 수도 있음
    def __str__(self):
        return str(self.order.order_date.date()) + f' ({str(self.order)}) ' + str(self.order.personal_information)


    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_menu_memo = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField()
