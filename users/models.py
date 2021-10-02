from django.db import models
# 기존 auth model을 커스텀하기 위한 방법
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, age, sex, phone, password):
        user = self.model(
            age=age,
            sex=sex,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
            age=None,
            sex=None,
            phone=phone,
            password=password,
        )
        user.is_superuser = True
        # user.is_staff = True
        user.save(using=self._db)
        return user


# 이전 User class
# class User(models.Model):
#     class Meta:
#         db_table = 'personal_information'
#
#     def __str__(self):
#         return self.phone
#
#     age = models.IntegerField()
#     sex = models.BooleanField(verbose_name='male')  # male=1, female=0
#     phone = models.CharField(max_length=11)
#     # pin->password
#     password = models.CharField(max_length=4)

class User(AbstractBaseUser, PermissionsMixin):
    age = models.IntegerField(null=True)
    sex = models.BooleanField(verbose_name='male', null=True)  # male=1, female=0
    phone = models.CharField(max_length=11, unique=True)
    # password = models.CharField(max_length=4)

    class Meta:
        db_table = 'personal_information'

    def __str__(self):
        return self.phone

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    # get_full_name.short_description = _('Full name')
