from instagrapi import Client
import random

client = Client()

client.login("yoour_sobass", "7^hjdFF84((df")

hastag = "travel"

comments = ["Awesome", "Great", "Nice"]

medias = client.hashtag_medias_recent(hastag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Like post number {i+1} of hastag {hastag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        
        client.media_comment(media.id, "Awesome post")

        comment = random.choice(comments)
        print(f"Commented {comment} under post number {i+1}")