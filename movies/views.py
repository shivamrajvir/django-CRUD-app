from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # ''.join([m.title for m in movies])
    # return HttpResponse(''.join([m.title for m in movies]))
    return render(request, 'movies/index.html', {"movies": movies})

