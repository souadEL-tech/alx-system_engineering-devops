#!/usr/bin/python3

"""
Function to query subscribers on a given Reddit subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """Set up the URL for the Reddit API endpoint for the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
