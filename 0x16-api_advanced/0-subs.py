#!/usr/bin/python3

"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """return the the total number of the subsctibers on a given subredddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, heades=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.hsin().get("data")
    return results.get("subscribers")
