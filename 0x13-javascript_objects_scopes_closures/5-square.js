#!/usr/bin/node
// exported class Square which inherits from imported Rectangle class
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
