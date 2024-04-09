#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && (!isNaN(w)) && w > 0 && typeof h === 'number' && (!isNaN(h)) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let tmp = 'X';
    for (let counter = 1; counter < this.width; counter++) {
      tmp = tmp.concat('X');
    }
    for (let counter = 0; counter < this.height; counter++) {
      console.log(tmp);
    }
  }

  rotate () {
    const tmpWidth = this.width;
    this.width = this.height;
    this.height = tmpWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
