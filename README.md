# funny-what3words
My friend noticed that sometimes the random what3words produced are quite humorous, so we wanted to see if we could find some more.

## How-to
1. Install the requirements from `requirements.txt` into a virtual environment. (N.B. **NOT** Python 3.12, a dependency of `openai` breaks).
2. Generate API keys for openai and for what3words and put them in a file called secrets.py as `WHAT3WORDS_API_KEY` and `OPENAI_API_KEY`.
3. You can now run the example script! You can expect an output something like:
```
Got contrive.inaugurated.stubbly for a spot at {'lng': -31.411847, 'lat': -74.895523}!
Contrive.inaugurated.stubbly may not be inherently funny, but with some clever context, it could potentially be hilariously interpreted as someone meticulously planning a stubble-growing ceremony.
```

More to come :)
