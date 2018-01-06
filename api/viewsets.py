from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from api.serializers import UserSerializer, GroupSerializer, DonationSerializer, RequestSerializer, DonationMatchSerializer, RequestMatchSerializer, CategorySerializer, SubCategorySerializer
#
from donationapp.models import Donation, Category, SubCategory, Request, DonationMatch, RequestMatch
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # this doesnt' work but it is the right idea
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.request.query_params['username'])
    #     return user

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Create your views here.
class DonationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class DonationMatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = DonationMatch.objects.all()
    serializer_class = DonationMatchSerializer

class RequestMatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows donations to be viewed and edited.
    """
    queryset = RequestMatch.objects.all()
    serializer_class = RequestMatchSerializer

# @api_view(["POST"])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})