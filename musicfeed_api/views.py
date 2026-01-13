from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import HttpRequest
from .services.DeezerApiService import DeezerApiService
# Create your views here.


def index(request):
    return HttpResponse("Welcome to musicfeed")


def getArtistRecords(request, artist_id: int):
    service = DeezerApiService()
    artist = service.find_artist_data(artist_id)
    if not artist:
        return HttpResponse("Artist not found.")
    return HttpResponse(f"Name : {artist.name}" + "\nAlbums : \n" 
                        + "\n".join([f"    {record.title} - {record.release_date}" for record in artist.records]))
