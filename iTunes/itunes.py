import json
import requests
import argparse
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit()
    parser = argparse.ArgumentParser(description='iTunes: Artist')
    parser.add_argument("-a", "--artist", action="store", required=True)
    args_dict = vars(parser.parse_args())
    args_str = args_dict["artist"]

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + args_str)

    # Change the + signs used in the URL back to space chars
    args_str = args_str.replace("+", " ")
    
    count = 0
    obj = response.json()
    for result in obj["results"]:
        if (result["artistName"] == args_str):
            print(result["trackName"])
            count += 1

    print( f"Total songs found: {count}")


if __name__ == "__main__":
    main()