from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from haversine import haversine, Unit

app = FastAPI()

origins = [
    "https://jryanhall94.github.io",
]

locations = {
    "white-house": {"lat": 38.897688, "lng": -77.036563},
    "gershwin": {"lat": 40.762062, "lng": -73.985062},
    "disney-world": {"lat": 28.377187, "lng": -81.570813},
    "alamo": {"lat": 29.425937, "lng": -98.486187},
    "cecil-hotel": {"lat": 34.044313, "lng": -118.250687},
    "machu-picchu": {"lat": -13.163068, "lng": -72.545128},
    "eiffel-tower": {"lat": 48.858312, "lng": 2.294437},
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)


class Coords(BaseModel):
    lat: float
    lng: float


def distance_between(point_a, point_b):
    return round(haversine(point_a, point_b, unit=Unit.MILES), 2)


@app.post("/coords/")
async def coords(coords: Coords):
    if coords.lat and coords.lng:

        return {
            "white-house": distance_between(
                locations["white-house"].values(), (coords.lat, coords.lng)
            ),
            "gershwin": distance_between(
                locations["gershwin"].values(), (coords.lat, coords.lng)
            ),
            "disney-world": distance_between(
                locations["disney-world"].values(), (coords.lat, coords.lng)
            ),
            "alamo": distance_between(
                locations["alamo"].values(), (coords.lat, coords.lng)
            ),
            "cecil-hotel": distance_between(
                locations["cecil-hotel"].values(), (coords.lat, coords.lng)
            ),
            "machu-picchu": distance_between(
                locations["machu-picchu"].values(), (coords.lat, coords.lng)
            ),
            "eiffel-tower": distance_between(
                locations["eiffel-tower"].values(), (coords.lat, coords.lng)
            ),
        }
