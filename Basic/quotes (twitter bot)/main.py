import tweepy
import random
import time

consumer_key = "W7QKrJF7mUWnswQqGQn7yGrw8"
consumer_secret = "spaJVC1Yzk2rLtj7cd5zPKOb8svpsbFbXOEgjBeC9eNMXhiuT1"
access_token = "1393064961748918282-mhXIbZwfkJM1KJN0vZDERiPMeXes3k"
access_token_secret = "ayr5MY1XrjmImkH0371WSTL5k5wSmiRBrM93bY50FFvZ9"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

poem = """Numa meia-noite agreste, quando eu lia, lento e triste,
Vagos, curiosos tomos de ciências ancestrais,
E já quase adormecia, ouvi o que parecia
O som de alguém que batia levemente a meus umbrais.
"Uma visita", eu me disse, "está batendo a meus umbrais.
É só isto, e nada mais."""

versos = poem.split("\n")

while True:
    verso_aleatorio = random.choice(versos)

    api.update_status(verso_aleatorio)

    time.sleep(3600)
