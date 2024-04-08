#!/usr/bin/node
const args = process.argv;
const count = 2;
if (typeof args[count] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[count]);
}
