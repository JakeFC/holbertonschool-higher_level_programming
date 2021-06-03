#!/usr/bin/node
/*
Rectangle class with 2 arguments that correspond to 2 attributes unless one
is 0 or less, then create empty object
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
