from django.db import models
from branches.models import Branch


# Create your models here.
class Ingredient(models.Model):
    class Meta:
        db_table = 'ingredient'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    origin = models.CharField(max_length=10)


class Menu(models.Model):
    class Meta:
        db_table = 'menu'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    menu_info = models.CharField(max_length=255, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    allergy_ingredient = models.IntegerField()
    ingredient = models.ManyToManyField(Ingredient)



# class NutritionFact(models.Model):
#     class Meta:
#         db_table = 'nutrition_fact'
#
#     def __str__(self):
#         return self.menu_id
#
#     menu_id = models.OneToOneField(Menu, on_delete=models.CASCADE,)
#     weight = models.IntegerField()
#     kcal = models.IntegerField()
#     sugars = models.IntegerField()
#     protein = models.IntegerField()
#     saturated_fat = models.IntegerField()
#     sodium = models.IntegerField()
#     caffeine = models.IntegerField(null=True)
