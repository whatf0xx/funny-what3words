from random import random
import what3words
import openai
from secrets import WHAT3WORDS_API_KEY, OPENAI_API_KEY

if __name__ == '__main__':
    x = (random() - 0.5) * 180
    y = (random() - 0.5) * 180
    coords = what3words.Coordinates(x, y)

    geocoder = what3words.Geocoder(WHAT3WORDS_API_KEY)
    package = geocoder.convert_to_3wa(coords)
    words, location = package["words"], package["coordinates"]
    print(f"Got {words} for a spot at {location}!")

    openai.api_key = OPENAI_API_KEY
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You run a humorous meme page and are skilled at finding witty word plays."},
            {"role": "user",
             "content": f"In a line or two, reason whether or not the word combination {words} is funny."}
        ]
    )

    print(completion.choices[0].message["content"])
