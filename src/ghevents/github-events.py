#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    '''
    Takes a single parameter, url, from which it retrieves events from the GitHub API.
    '''
    return json.loads(requests.get(url).text)

def print_events(events, n=5):
    '''
    Loops over the first n events (default is 5) and prints the event type and the repo name.
    '''
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    '''
    Prints the GitHub user and the URL to the events, as well as the first 5 events' type and repo name.
    '''
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()