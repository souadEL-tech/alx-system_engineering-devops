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
        # Make a GET request to the subreddit about endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or any error occurs, return 0
            return 0
    except requests.RequestException:
        # If there is a network-related error, return 0
        return 0
