from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register('', views.Branches_view_set)

urlpatterns = router.urls
