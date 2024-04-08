#!/usr/bin/node
const input = process.argv[2];
const size = parseInt(input);
if (typeof size !== 'number' || isNaN(size)) {
  console.log('Missing size');
} else {
  let output = 'X';
  for (let i = 1; i < size; i++) {
    output = output.concat('X');
  }
  for (let j = 0; j < size; j++) {
    console.log(output);
  }
}
