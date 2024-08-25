#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
    else:
        print("Please provide a subreddit name.")
