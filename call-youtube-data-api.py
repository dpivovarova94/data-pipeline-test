# Calling Omdb API: https://apilist.fun/api/omdb
# import requests

# APIKey = "4d8b770c"
# url = 'https://www.omdbapi.com/'
# params = {
#     'apikey': APIKey,
#     't': 'The Matrix'  # Replace with the title you want to search for
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# Extract the comment threads of a given youtube video
import os
from googleapiclient.discovery import build
import pandas as pd

# def main():
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = "AIzaSyBbhKLpifhG7lm9T0LKaKHu9dAO0oEGGXE"

#     youtube = build(
#         api_service_name, api_version, developerKey = DEVELOPER_KEY)

#     request = youtube.commentThreads().list(
#         videoId="q8q3OFFfY6c",
#         part="snippet,replies"
#     )
#     response = request.execute()

#     # print(response)
#     response_items = response.get('items', [])
#     print(response_items['snippet']['topLevelComment'])
#     print(response_items)


# if __name__ == "__main__":
#     main()

# ---------------------------TESTING----------------------
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBbhKLpifhG7lm9T0LKaKHu9dAO0oEGGXE"

youtube = build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.commentThreads().list(
    videoId="q8q3OFFfY6c",
    part="snippet,replies"
)
response = request.execute()

# print(response)
response_items = response['items']
# print(response_items['snippet']['topLevelComment'])
# print(response_items)


# Transform the data

def process_comments(response_items):
		comments = []
		for comment in response_items:
				author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
				comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
				publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
				comment_info = {'author': author, 
						'comment': comment_text, 'published_at': publish_time}
				comments.append(comment_info)
		print(f'Finished processing {len(comments)} comments.')
		return comments

comments = process_comments(response_items)

# Loading the Data
df = pd.DataFrame(comments)
df.to_csv("youtube_comment_data.csv")