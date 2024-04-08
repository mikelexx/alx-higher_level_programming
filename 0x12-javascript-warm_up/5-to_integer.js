#!/usr/bin/node
const arg = process.argv[2];
const converted = parseInt(arg);
if (typeof converted !== 'number' || isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(converted));
}
