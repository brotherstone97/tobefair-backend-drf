from rest_framework import serializers
from .models import Ingredient, Menu

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True, read_only=True) #post시 새로 만든 ingredient필드가 영향을 미치지 않도록 read-only=True로 함
    class Meta:
        model = Menu
        fields = ['id','name','image','price','menu_info','menu_type','allergy_ingredient','branch_id','ingredient']
