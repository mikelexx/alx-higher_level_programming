#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request
    print("Body response:")
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
