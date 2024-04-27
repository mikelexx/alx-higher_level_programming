#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    values = ''
    if len(sys.argv) >= 2:
        values = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': values})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError as e:
        print("Not a valid JSON")
