**Resources**

Read or watch:

- [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
- [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
- [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module
**More Info**

Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
**Install semi-standard**
-[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)
```
$ sudo npm install semistandard --global
```
**Install request module and use it**
- [Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
-[if you have difficulty in installing requests](https://stackoverflow.com/questions/16482600/node-js-cannot-find-module-request)

Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

**Tasks**
0. Readme
mandatory
Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$
```
File: `0-readme.js`

1. Write me
mandatory
Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the error object
```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$
```
File: `1-writeme.js`

2. Status code
mandatory
Write a script that display the status code of a GET request.

- The first argument is the URL to request (GET)
- The status code must be printed like this: code: <status code>
- You must use the module request
```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$
```
File: `2-statuscode.js`

3. Star wars movie title
mandatory
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
- You must use the module request
```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$
```

File: `3-starwars_title.js`

4. Star wars Wedge Antilles
mandatory
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
- You must use the module request
```
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$
```

File: `4-starwars_count.js`
