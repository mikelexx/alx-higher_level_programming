**Resources**
Read or watch:

- [HOWTO Fetch Internet Resources Using urllib Package](https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ)
- [Quickstart with Requests package](https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ)
- [Requests package](https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ)
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

**Tasks**
0. What's my status? #0
mandatory
Write a Python script that fetches https://alx-intranet.hbtn.io/status

- You must use the package urllib
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed like the following example (tabulation before -)
	```
- You must use a with statement
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
```
File: `0-hbtn_status.py`

