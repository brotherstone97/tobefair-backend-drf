from rest_framework import routers
from django.conf.urls import url, include
from . import views
router = routers.DefaultRouter()
router.register(r'order_menus', views.Order_menu_view_set)
router.register(r'payments', views.Payment_view_set)
router.register(r'', views.Order_view_set)


urlpatterns = router.urls
