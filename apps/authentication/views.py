from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict,JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from .serializers import AuthorSerializer
from .models import Author
from django.contrib.auth.models import User
from .jwt import get_token,get_payload
import json

# Create your views here.

@csrf_exempt
@api_view(['GET','POST','PUT'])
def user_operations(request):

    if request.method == 'POST':
        user_obj = json.loads(request.POST['user'])
        username = user_obj.get('username')
        email = user_obj.get('email')
        password = user_obj.get('password')

        try:
            user = User.objects.create_user(username,email=email,password=password)
            user.is_superuser=False
            user.is_staff=False
            user.save()
            author = Author(user=user)
            author.token = str(get_token({'user_id' : user.id}))
            author.save()
        except:
            error_response = JsonResponse({"errors" : {"body" : ["Unexpected Error"]}})
            error_response.status_code=422
            return error_response

        success_response = JsonResponse({"user" : {"email" : user.email,"token" : user.author.token, "username" : user.username , "bio" : user.author.bio , "image" : user.author.image}})
        success_response.status_code=201
        return success_response

    elif request.method == 'GET':
        try:
            token = request.META['HTTP_AUTHORIZATION']
        except:
            error_response = JsonResponse({"errors" : {"body" : ["Unauthorized"]}})
            error_response.status_code=401
            return error_response

        try:
            payload = get_payload(token)
            user = User.objects.get(pk=payload["user_id"])

        except:
            error_response = JsonResponse({"errors" : {"body" : ["Unexpected Error"]}})
            error_response.status_code=422
            return error_response

        success_response = JsonResponse({"user" : {"email" : user.email,"token" : user.author.token, "username" : user.username , "bio" : user.author.bio , "image" : user.author.image}})
        success_response.status_code=201
        return success_response
