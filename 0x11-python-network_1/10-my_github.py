#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
import base64

if __name__ == "__main__":
    token = sys.argv[2]
    auth_token = base64.b64encode(f"{sys.argv[1]}:{token}".encode()).decode()
    headers = {
        'Authorization': f"Basic {auth_token}",
        "Accept": "application/vnd.github+json"
    }

    r = requests.get('https://api.github.com/user', headers=headers)
    response = r.json()
    user_id = response.get("id")
    print(user_id)
