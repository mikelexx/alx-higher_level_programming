#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request
    print("Body response:")
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        print("\t- type: {}".format(type(response.read())))
        print("\t- content: {}".format(response.read()))
        print("\t- utf8 content: {}".format(response.read().decode()))
