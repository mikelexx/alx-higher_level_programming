#!/usr/bin/node
const args = process.argv;
let count = 0;
if (args.length <= 3) {
  console.log(0);
} else {
  while (count < 2) {
    for (let i = 2; i < args.length - 1; i++) {
      if (args[i] > args[i + 1]) {
        const tmp = args[i];
        args[i] = args[i + 1];
        args[i + 1] = tmp;
      }
    }
    count++;
  }
  console.log(args[args.length - 2]);
}
