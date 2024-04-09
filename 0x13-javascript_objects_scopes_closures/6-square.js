#!/usr/bin/node
const ParentSquare = require('./5-square');
module.exports = class Square extends ParentSquare {
  charPrint (c) {
    let delimiter = c;
    if (typeof delimiter === 'undefined') {
      delimiter = 'X';
    }
    let tmp = delimiter;
    for (let count = 1; count < this.width; count++) {
      tmp = tmp.concat(delimiter);
    }
    for (let count = 0; count < this.height; count++) {
      console.log(tmp);
    }
  }
};
