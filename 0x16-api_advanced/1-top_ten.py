#!/usr/bin/python3


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            posts = data['data']['children']
            if not posts:
                print(None)
                return

            for post in posts:
                print(post['data']['title'])
        else:
            print(None)

    except requests.RequestException:
        print(None)
