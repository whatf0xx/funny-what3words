from random import random
from typing import Generator
from collections import namedtuple
from time import sleep
from what3words import Coordinates, Geocoder


W3wTuple = namedtuple('W3wTuple', 'words, lng, lat')


def get_random_w3w(api_key: str) -> Generator[W3wTuple, None, None]:
    geocoder = Geocoder(api_key)
    while True:
        x = (random() - 0.5) * 180
        y = (random() - 0.5) * 180
        coords = Coordinates(x, y)

        package = geocoder.convert_to_3wa(coords)
        words, location = package["words"], package["coordinates"]
        lng, lat = location['lng'], location['lat']
        rtn = W3wTuple(words, lng, lat)
        # print(rtn)
        yield rtn
