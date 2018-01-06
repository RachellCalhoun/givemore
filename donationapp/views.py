from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.
def donate(request):
	return render(request, 'donationapp/index.html')

# @api_view(["POST"])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})