**Concepts**
For this project, we expect you to look at these concepts:

- [JavaScript in the browser](https://intranet.alxswe.com/concepts/3)
- [Dealing with data statically versus dynamically](https://intranet.alxswe.com/concepts/35)

![Jquery Meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)
**Read or watch**
- [What is JavaScript?](https://intranet.alxswe.com/rltoken/NJ5XM_fzjlBKERHTkdF-uA)
- [Selector](https://intranet.alxswe.com/rltoken/wsnVUxEcAzzlCx6ES1qc7g)
- [Get and set content](https://intranet.alxswe.com/rltoken/rwtc96sn2_LHToBAd0MIhQ)
- [Manipulate CSS classes](https://intranet.alxswe.com/rltoken/IcM5kKVzssU0ibdUo-2gKQ)
- [Manipulate DOM elements](https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ)
- [API](https://intranet.alxswe.com/rltoken/vKc7XmiHG7HIh3N0Kl_VQw)
- [Introduction](https://intranet.alxswe.com/rltoken/QiUwuS_9TXE49D5IVL-ocg)
- [GET & POST request](https://intranet.alxswe.com/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.alxswe.com/rltoken/gMwyXisSLu-kZicmGA0-LQ)
- [What went wrong? Troubleshooting JavaScript](https://intranet.alxswe.com/rltoken/4eYyJr72PO-cohImk93M3w)
- [JQuery](https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw)
- [JQuery API](https://intranet.alxswe.com/rltoken/jvibhq-8VEdQHNUWKTCI7w)
- [JQuery Ajax](https://intranet.alxswe.com/rltoken/rBZyrXxuRuISDfPBzO9Y7Q)

**Learning Objectives**

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a GET request with JQuery Ajax
- How to make a POST request with JQuery Ajax
- How to listen/bind to DOM events
- **How to listen/bind to user events**
** More info**
**Import JQuery **
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```
![JQUERY Meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

**Tasks**

0. No JQuery
mandatory
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You must use document.querySelector to select the HTML tag
- You can’t use the JQuery API
Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 0-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header>
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$
```
File: `0-script.js`

