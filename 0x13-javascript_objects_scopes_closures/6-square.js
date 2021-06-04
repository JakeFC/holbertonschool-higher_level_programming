#!/usr/bin/node
// exported class Square which inherits from imported Rectangle class
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    c ? c = c : c = 'X';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
