#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
	  if (typeof w === 'number' && (!isNaN(w)) && w > 0 && typeof h === 'number' && (!isNaN(h)) && h > 0) {
		  this.width = w;
		  this.height = h;
	  }
  }
};
