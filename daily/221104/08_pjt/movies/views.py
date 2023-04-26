from .models import Movie
from django.shortcuts import render
from django.views.decorators.http import require_safe
import random
from django.db.models import Max
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)



@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def recommended(request):
    max_id = Movie.objects.all().aggregate(max_id=Max('id'))['max_id']
    
    
    movies=[]
    while len(movies)<3:
        num=random.randint(1,max_id)
        tmp=Movie.objects.get(pk=num)
        if tmp.popularity>=80:
            if tmp not in movies:
                movies.append(tmp)
        
        

    context={

        'movies':movies,
    }
    return render(request,'movies/recommended.html', context)