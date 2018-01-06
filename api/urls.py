from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)
router.register(r'donations', viewsets.DonationViewSet)
router.register(r'donationmatches', viewsets.DonationMatchViewSet)
router.register(r'requests', viewsets.RequestViewSet)
router.register(r'requestmatches', viewsets.RequestMatchViewSet)
router.register(r'categories', viewsets.CategoryViewSet)
router.register(r'subcategories', viewsets.SubCategoryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]