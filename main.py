from enum import Enum

from fastapi import FastAPI

from DeezerApiService import DeezerApiService


class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()
service = DeezerApiService()


@app.get("/")
async def root():
    return {"message": "hello world."}


@app.get("/artist/{artist_id}")
async def model_name(artist_id: int):
    data = service.find_artist_data(artist_id)
    print(f"data:{data}")
    return {"data": data}
