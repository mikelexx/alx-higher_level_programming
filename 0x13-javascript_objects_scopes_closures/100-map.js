#!/usr/bin/node
const list = require('./100-data').list;
const res = list.map((el, idx) => el * idx);
console.log(list);
console.log(res);
