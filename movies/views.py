from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # ''.join([m.title for m in movies])
    # return HttpResponse(''.join([m.title for m in movies]))
    return render(request, 'movies/index.html', {"movies": movies})


def detail(request, movie_id):
    # try:
    #     # pk = primary key
    #     movieDetail = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/details.html', {"movie": movieDetail})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/details.html', {"movie": movie})