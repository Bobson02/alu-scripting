#!/usr/bin/python3
"""Queries the Reddit API for the top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    # Make the request
    response = requests.get(reddit_url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print("OK")
