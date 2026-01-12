from typing import Optional
import requests
from dataclasses import dataclass

@dataclass
class RecordData():
    record_id : int
    title : str
    release_date : str

@dataclass
class ArtistData():
    deezer_id: int
    name: str
    records = list[RecordData]



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
            records_list_json = self.session.get(
                self.BASE_URL + f""
            )


            return ArtistData(deezer_id, name)
        except Exception:
            return None
