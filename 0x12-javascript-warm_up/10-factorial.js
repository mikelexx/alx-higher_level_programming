#!/usr/bin/node
let input = process.argv[2];
input = parseInt(input);
function factorial (a) {
  if (a === 1 || a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
if (isNaN(input)) {
  console.log(1);
} else {
  console.log((factorial(input)));
}
