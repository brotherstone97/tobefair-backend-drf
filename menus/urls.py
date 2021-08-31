from rest_framework import routers
from django.conf.urls import url, include
from . import views
router = routers.DefaultRouter()
router.register(r'ingredients', views.Ingredients_view_set)
router.register('', views.Menus_view_set)

urlpatterns = router.urls
