import random

with open("tweets.txt", encoding="utf-8") as f:
    tweets = [x.strip() for x in f if x.strip()]

print(random.choice(tweets))
