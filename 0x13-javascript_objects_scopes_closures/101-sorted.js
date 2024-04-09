#!/usr/bin/node
const mDict = require('./101-data').dict;
const res = {};
for (const key in mDict) {
  if (typeof res[mDict[key]] === 'undefined') {
    res[mDict[key]] = [];
  }
  res[mDict[key]].push(key);
}
console.log(res);
