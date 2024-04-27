#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
It also manages urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import sys
    from urllib.error import URLError
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code: ', e.code)
