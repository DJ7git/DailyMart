from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from AdminApp.models import Article
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import *


# Create your views here.

def defaultAdmin(request):
    return HttpResponse('Hello World from Admin App page')

def aindex(request):
    		return render(request,'aindex.html')

def add(request):
    		return render(request,'add.html')

def getdata(request):
	if request.method == 'POST':
		movieName1 = request.POST['movieName']
		movieImage1 = request.FILES['movieImage']
		movieGenre1 = request.POST['movieGenre']
		movieLanguage1 = request.POST['movieLanguage']
		movieDescription1 = request.POST['movieDescription']
		data = Movie(movieName=movieName1,movieImage=movieImage1,movieGenre=movieGenre1,movieLanguage=movieLanguage1,movieDescription=movieDescription1)
		data.save()
	return redirect("add")

def view(request):
	data = Movie.objects.all()
	return render(request,'view.html',{'viewdata':data})

def editdata(request,id):
    data = Movie.objects.filter(id=id)
    return render(request,'edit.html',{'dataedit':data})

def update(request,id):
	if request.method == 'POST':
		movieName1 = request.POST['movieName']
		movieGenre1 = request.POST['movieGenre']
		movieLanguage1 = request.POST['movieLanguage']
		movieDescription1 = request.POST['movieDescription']
		try:
			img_c = request.FILES['movieImage']
			fs = FileSystemStorage()
			movieImage1 = fs.save(img_c.name, img_c)
		except MultiValueDictKeyError:
			movieImage1 = Movie.objects.get(id=id).movieImage
		
		Movie.objects.filter(id=id).update(movieName=movieName1,movieImage=movieImage1,movieGenre=movieGenre1,movieLanguage=movieLanguage1,movieDescription=movieDescription1)
	
	return redirect("view")

def delete(request,id):
    Movie.objects.filter(id=id).delete()
    return redirect("view")

from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer

def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles,many=True)
		return JsonResponse (serializer.data, safe=False)
	elif request.method == 'POST':
		data = JsonResponse().Parse(request)
		serializer = ArticleSerializer(data=data)
		if serializer.is_valid():
			# serializer.save()
			Article.objects.create(**serializer.validated_data)
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)
	
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def article_details(request,pk):
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return HttpResponse(status = 404)

	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return JsonResponse (serializer.data)
	elif request.method == 'PUT':
		data = JsonResponse().Parse(request)
		serializer = ArticleSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)
	
	elif request.method == 'DELETE':
		article.delete()
		return HttpResponse(status=204)

class MyView(APIView):
	def post(self, request):
		data = request.data  # This will contain the POST data
        # Do something with the data here\
		return Response({"message": "Data received", "data": data}, status=status.HTTP_201_CREATED)