#!/usr/bin/node
/*
exported Rectangle class with 2 args that correspond to 2 attributes and a
method if they're both over 0
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let y = 0; y < h; y++) {
          for (let x = 0; x < w; x++) {
            process.stdout.write('X');
          }
          console.log();
        }
      };
    }
  }
};
