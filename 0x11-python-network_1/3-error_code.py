#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
It also manages urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
if __name__ == "__main__":
    import urllib.request
    try:
        with urllib.request.urlopen('http://python.org/') as response:
            html_bytes = response.read()
            print(html_bytes.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {} '.format(e.code))
