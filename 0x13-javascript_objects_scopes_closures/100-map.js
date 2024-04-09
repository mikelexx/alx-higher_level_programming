#!/usr/bin/node
const list = require('./100-data').list;
const res = list.map(el => el * list.indexOf(el));
console.log(list);
console.log(res);
