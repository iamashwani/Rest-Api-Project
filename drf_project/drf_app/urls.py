from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'phonenumbers', views.PhoneNumberViewSet)
router.register(r'spamnumbers', views.SpamNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

