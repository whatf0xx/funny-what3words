from random import random
import what3words
from secrets import WHAT3WORDS_API_KEY

if __name__ == '__main__':
    x = (random() - 0.5) * 180
    y = (random() - 0.5) * 180
    coords = what3words.Coordinates(x, y)

    geocoder = what3words.Geocoder(WHAT3WORDS_API_KEY)
    package = geocoder.convert_to_3wa(coords)
    words, location = package["words"], package["coordinates"]
    print(f"Got {words} for a spot at {location}!")
