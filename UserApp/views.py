from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from AdminApp.models import *
from UserApp.models import Article


# Create your views here.

def defaultuser(request):
    return HttpResponse('Hello World from User App page')

def uindex(request):
    		return render(request,'uindex.html')


def viewsingledata(request,id):
    data = Movie.objects.filter(id=id)
    return render(request,'viewsingle.html',{'datasingle':data})

def viewuser(request):
	data = Movie.objects.all()
	return render(request,'viewuser.html',{'viewdata':data})

# import @api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET','POST'])
def article_list(request):
        if request.method == 'GET':
                articles = Article.objects.all()
                serializer = ArticleSerializer(articles,many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    