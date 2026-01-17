from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from .services.DeezerApiService import DeezerApiService
# Create your views here.
from api.models import User, Following


def index(request):
    return HttpResponse("Welcome to musicfeed")


def getArtistRecords(request, artist_id: int):
    service = DeezerApiService()
    artist_data = service.find_artist_data(artist_id)
    if not artist_data:
        return JsonResponse({"error": "Artist not found."})
    return JsonResponse(artist_data.to_dict())


def getUserFeed(request, username: str):
    if username not in [u.username for u in User.objects.all()]:
        return JsonResponse({
            "error": "user not found"
        })
    user = User.objects.get(username=username)
    followed_artists_ids = [
        r.artist_id for r in Following.objects.filter(username=user)]
    artists_data = []
    service = DeezerApiService()
    for deezer_id in followed_artists_ids:
        data = service.find_artist_data(deezer_id=deezer_id)
        if data:
            artists_data.append(data)

    return JsonResponse({
        "id": user.id,
        "username": user.username,
        "phone_number": user.phone_number,
        "feed": [data.to_dict() for data in artists_data]
    })
