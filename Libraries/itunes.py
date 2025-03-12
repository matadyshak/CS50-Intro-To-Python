import requests
import sys
import json
import argparse

parser = argparse.ArgumentParser(description="Query iTunes")
parser.add_argument("--artist", action="store", dest=artist, type=str)
args = parser.parse_args()

if len(args) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + args.artist)

o = response.json()
for result in o["results"]:
    #print(json.dumps(response.json(), indent=2))
    if(result["artistName"] == args._get_args):
        print(result["trackName"])