from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:artist_id>/", views.getArtistRecords, name="artist"),
    path("user/<str:username>/feed", views.getUserFeed,name="user_feed")
]