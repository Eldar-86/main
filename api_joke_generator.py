import time
import requests


while True:
    joke = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    ).json()
    try:
        if joke["type"] == "twopart":
            print(f"- {joke['setup']}")
            time.sleep(4)
            print(f"- {joke['delivery']}\n")
            time.sleep(4)
        else:
            print(f"{joke['joke']}\n")
            time.sleep(8)
    except KeyError:
        print("0")
        break
