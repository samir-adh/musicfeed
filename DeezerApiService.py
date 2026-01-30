from typing import Any, Optional

import requests
from pydantic import BaseModel


class RecordData(BaseModel):
    record_id: int
    title: str
    release_date: str
    record_type: str

    def to_dict(self) -> dict[str, Any]:
        return {"title": self.title, "release_date": self.release_date}


class ArtistData(BaseModel):
    deezer_id: int
    name: str
    records: list[RecordData]

    def addRecord(self, record: RecordData):
        self.records.append(record)

    def to_dict(self):
        return {
            "name": self.name,
            "albums": [record.to_dict() for record in self.records],
        }


class APIDataNotFoundError(Exception):
    """Raised when expected data is missing from API response"""

    pass


class DeezerApiService:
    BASE_URL = "https://api.deezer.com"

    def __init__(self) -> None:
        self.session = requests.Session()

    def find_artist_data(self, deezer_id: int) -> Optional[ArtistData]:
        response = self.session.get(self.BASE_URL + f"/artist/{deezer_id}", timeout=5)
        if "error" in response.json():
            return None
        deezer_id = response.json()["id"]
        name = response.json()["name"]

        artist = ArtistData(deezer_id=deezer_id, name=name,records=[])
        self.resolve_albums_list(artist)
        return artist

    def resolve_albums_list(self, artist: ArtistData):
        response = self.session.get(
            self.BASE_URL + f"/artist/{artist.deezer_id}/albums/"
        )
        if (
            "error" in response.json()
            and response.json()["error"]["type"] == "DataException"
        ):
            raise APIDataNotFoundError()
        albums_list = response.json()["data"]
        for record_data in albums_list:
            record = RecordData(
                record_id=record_data["id"],
                title=record_data["title"],
                release_date=record_data["release_date"],
                record_type=record_data["record_type"],
            )
            artist.addRecord(record)
