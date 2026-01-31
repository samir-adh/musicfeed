from fastapi import FastAPI

from lib.DeezerApiService import DeezerApiService

app = FastAPI()
service = DeezerApiService()

database_users = [
    {
        "name": "samiradh",
        "follows": [
            "1518490",  # A$AP Rocky
            "4105259",  # Joey Bada$$
            "67211132",  # Ben plg
            "13797255",  # Huntrill
            "1042268",  # Angèle
            "6043160",  # Kali Uchis
        ],
    }
]


@app.get("/")
async def root():
    return {"message": "hello world."}


@app.get("/artist/{artist_id}")
async def get_artist(artist_id: int, since: str | None = None):
    try:
        data = service.get_artist_data(artist_id, since)
    except ValueError:
        return {"error": "invalid date format"}

    return {"data": data}


@app.get("/search")
async def search_artist(query: str):
    data = service.search_artist(query)
    return data


@app.get("/feed/{username}")
async def get_user_feed(username: str):
    # Find user
    user = None
    for item in database_users:
        if item["name"] == username:
            user = item
    if not user:
        return {"error": "user not found"}

    # Get data for all artists followed by user
    artists_data = []
    for artist_id in user["follows"]:
        if data := service.get_artist_data(artist_id):
            artists_data.append(data)
    return artists_data
