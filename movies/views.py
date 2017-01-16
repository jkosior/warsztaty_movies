from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie, Person
from movies.serializers import MovieSerializer, PersonSerializer
from django.http.response import Http404
from rest_framework import status



# Create your views here.
class MoviesView(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True, context = {'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
        
class MovieView(APIView):
    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk = pk)           
        except Movie.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie,context = {"request": request})
        return Response(serializer.data)
    
    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    def put(self, request,pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class PersonsView(APIView):
    
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        persons = Person.objects.all()
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
        
class PersonView(APIView):
    
    def get_object(self, pk):
        try:
            return Person.objects.get(pk = pk)           
        except Person.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person,context = {"request": request})
        return Response(serializer.data)
    
    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    def put(self, request,pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)