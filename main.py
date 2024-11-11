import openai
from secrets import WHAT3WORDS_API_KEY, OPENAI_API_KEY
from fw3w import get_random_w3w

if __name__ == '__main__':
    random_w3w_generator = get_random_w3w(WHAT3WORDS_API_KEY)
    for _ in range(10):
        words, lng, lat = next(random_w3w_generator)
        print(f"Got {words} for a spot at {lng=}, {lat=}!")

    # openai.api_key = OPENAI_API_KEY
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system",
    #          "content": "You run a humorous meme page and are skilled at finding witty word plays."},
    #         {"role": "user",
    #          "content": f"In a line or two, reason whether or not the word combination {words} is funny."}
    #     ]
    # )
    #
    # print(completion.choices[0].message["content"])
