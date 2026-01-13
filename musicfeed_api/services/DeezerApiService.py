from typing import Optional
import requests
from dataclasses import dataclass
from enum import Enum


@dataclass
class RecordData():
    record_id: int
    title: str
    release_date: str
    record_type: str


class ArtistData():

    def __init__(self, deezer_id: int, name: str) -> None:
        self.deezer_id: int = deezer_id
        self.name: str = name
        self.records: list[RecordData] = []

    def addRecord(self, record: RecordData):
        self.records.append(record)


class APIDataNotFoundError(Exception):
    """Raised when expected data is missing from API response"""
    pass


class DeezerApiService():
    BASE_URL = "https://api.deezer.com"

    def __init__(self) -> None:
        self.session = requests.Session()

    def find_artist_data(self, deezer_id: int) -> Optional[ArtistData]:
        try:
            response = self.session.get(
                self.BASE_URL + f"/artist/{deezer_id}",
                timeout=5
            )
            if "error" in response.json():
                return None
            deezer_id = response.json()["id"]
            name = response.json()["name"]

            artist = ArtistData(deezer_id, name)
            self.resolve_albums_list(artist)
            return artist
        except Exception:
            return None

    def resolve_albums_list(self, artist: ArtistData):
        response = self.session.get(
            self.BASE_URL + f"/artist/{artist.deezer_id}/albums/"
        )
        if "error" in response.json() and response.json()["error"]["type"] == "DataException":
            raise APIDataNotFoundError
        albums_list = response.json()["data"]
        for record_data in albums_list:
            record = RecordData(
                record_data["id"],
                record_data["title"],
                record_data["release_date"],
                record_data["record_type"]
            )
            artist.addRecord(record)
