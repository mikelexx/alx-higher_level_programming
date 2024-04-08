#!/usr/bin/node
const args = process.argv;
let count = 2;
if (typeof args[count] === 'undefined'){
	console.log('No argument');
	return;
}
while (typeof args[count] !== 'undefined') {
  console.log(args[count]);
  count++;
}
