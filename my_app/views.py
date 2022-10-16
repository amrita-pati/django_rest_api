from django.shortcuts import render
from email.headerregistry import Address
from django.shortcuts import loader, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def addition(request):
    try:
        num1=int(request.data.get('num1'))
        num2=int(request.data.get('num2'))
        sum1 = num1+num2
        return Response({"status":"Success","message":f"Addition Result : {sum1}"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})
   
@api_view(['POST'])
def division(request):
    try:
        num1=int(request.data.get('num1'))
        num2=int(request.data.get('num2'))
        div = num1/num2
        return Response({"status":"Success","message":f"division Result : {div}"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})
   
