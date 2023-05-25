# Importing library
from instagrapi import Client
import random

INSTAGRAM_USER = "Enter your user id"
INSTAGRAM_PASSWORD = "Enter your ig password"

client = Client()
client.login(INSTAGRAM_USER, INSTAGRAM_PASSWORD)

hastag = "photography"
# hastag = ["naturelover", "nature", "naturephotography", "naturelovers", "photography", "travel", "perfection", "Love", "ig", "travelphotography", "wildlife", "flowers", "sunset", "trending", "natureview" "sky" ]

comments = ["Awesome", "Great", "Nice"]

medias = client.hashtag_medias_recent(hastag, 20)

for i, media in enumerate(medias):
    # liking in the post
    client.media_like(media.id)

    # hastag = random.choice(hastag)
    print(f"Like post number {i+1} of hastag {hastag}")
    # follow the user
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        
        # commeent on the user post
        client.media_comment(media.id, "Awesome post")
        comment = random.choice(comments)
        print(f"Commented {comment} under post number {i+1}")