#!/usr/bin/node
const arg = process.argv[2];
const converted = parseInt(arg);
if (typeof converted !== 'number' || isNaN(converted)) {
  console.log('Missing number of occurrences');
} else {
  let count = converted;
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
