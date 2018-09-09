from django.shortcuts import render,HttpResponse
from . import lyricsScrap
# Create your views here.


def index(request):
    return render(request,'lyrics/index.html')

def lyrics(request):
    artist = request.GET['artist']
    song= request.GET['song']
    lyrics = lyricsScrap.get_lyrics(artist,song)

    context= {
        'title': song,
        'content': lyrics,
    }

    return render(request,'lyrics/lyrics.html',context)