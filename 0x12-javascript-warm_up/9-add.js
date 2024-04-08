#!/usr/bin/node
let first = process.argv[2];
first = parseInt(first);
let second = process.argv[3];
second = parseInt(second);
function add (a, b) {
  return (a + b);
}
console.log(add(first, second));
