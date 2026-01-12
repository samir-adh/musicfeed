from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import HttpRequest
from .services.DeezerApiService import DeezerApiService
# Create your views here.
def index(request):
    return HttpResponse("Welcome to musicfeed")

def getArtistRecords(request, artist_id: int):
    service = DeezerApiService()
    artist_data = service.find_artist_data(artist_id)
    if not artist_data:
        return HttpResponse("Artist not found.")
    return HttpResponse(artist_data.name)