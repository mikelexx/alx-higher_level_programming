Resources
Read or watch:
- [JavaScript object basics](https://intranet.alxswe.com/rltoken/dsSkBB-Cj0tqUFL8eOZLLQ)
- [Object-oriented JavaScript (read all examples!)](https://intranet.alxswe.com/rltoken/qqgqdyHPzUZkKQ5UMnw2MQ)
- [Class - ES6](https://intranet.alxswe.com/rltoken/NEm-UViCThD5hfq_3Lj9Hg)
- [super - ES6](https://intranet.alxswe.com/rltoken/_cxdVKsdqPWbbp2cHtQSbQ)
- [extends - ES6](https://intranet.alxswe.com/rltoken/6wdl6Bc5yjBplpiZKmr6Zw)
- [Object prototypes](https://intranet.alxswe.com/rltoken/NiBbDiOlfhfUf4eIigglIw)
- [Inheritance in JavaScript](https://intranet.alxswe.com/rltoken/NiBbDiOlfhfUf4eIigglIw)
- [Closures](https://intranet.alxswe.com/rltoken/CybTMKEDNdTdU99kx_OXgQ)
- [this/self](https://intranet.alxswe.com/rltoken/XcOkisoKPud4faDDkLMABw)
- [Modern JS](https://intranet.alxswe.com/rltoken/rU_q2J3qGWfvTYNllW8JnA)
- [Function Binding](https://javascript.info/bind#:~:text=bind(context%2C%20...,For%20example%2C%20to%20setTimeout%20.)
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another
-----------------------------------------
**TASKS**
0. Rectangle #0
- Write an empty class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
```
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 

```
======================================
1. Rectangle #1

- Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
	- The constructor must take 2 arguments w and h
	- Initialize the instance attribute width with the value of w
	- Initialize the instance attribute height with the value of h
```
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$

```
2. Rectangle #2
- Write a class Rectangle that defines a rectangle:

	- You must use the class notation for defining your class
	- The constructor must take 2 arguments w and h
	- Initialize the instance attribute width with the value of w
	- Initialize the instance attribute height with the value of h
	- If w or h is equal to 0 or not a positive integer, create an empty object.
```
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$
```
3. Rectangle #3
- Write a class Rectangle that defines a rectangle:
- 
	- You must use the class notation for defining your class
	- The constructor must take 2 arguments: w and h
	- Initialize the instance attribute width with the value of w
	- Initialize the instance attribute height with the value of h
	- If w or h is equal to 0 or not a positive integer, create an empty object
	- Create an instance method called print() that prints the rectangle using the character X
```
	guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$
```
4. Rectangle #4
- Write a class Rectangle that defines a rectangle:

	- You must use the class notation for defining your class
	- The constructor must take 2 arguments: w and h
	- Initialize the instance attribute width with the value of w
	- Initialize the instance attribute height with the value of h
	- If w or h is equal to 0 or not a positive integer, create an empty object
	- Create an instance method called print() that prints the rectangle using the character X
	- Create an instance method called rotate() that exchanges the width and the height of the rectangle
	- Create an instance method called double() that multiples the width and the height of the rectangle by 2
```
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$
```
