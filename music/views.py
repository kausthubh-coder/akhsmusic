from django.shortcuts import render
from .models import Song

# Create your views here.
def index(request):
    return render(request, 'index.html')


def songs(request):
    song = Song.objects.all
    return render(request, 'songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id)
    return render(request, 'songpost.html', {'song': song})


# def search(request):
#     query = request.GET.get("query")
#     song = Song.objects.all(name=query)
#     return render(request, 'search.html', {'song': qs})

# def search(request):
#     if request.GET.get('myform'): # write your form name here      
#         song_name =  request.GET.get('myform')      
#         try:
#             song = Song.objects.filter(name__icontains=song_name)
#             return render(request,"search.html",{"song":song})
#         except:
#             return render(request,"search.html",{'song':song})
#     else:
#         return render(request, 'songs.html')


def search(request):
    query = request.GET.get("query")
    song = Song.objects.filter(name="query")
    return render(request, 'songs.html', {'song': song})

def sup(request):
    return render(request, 'sup.html')