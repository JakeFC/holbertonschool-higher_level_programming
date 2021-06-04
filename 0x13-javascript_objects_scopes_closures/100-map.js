#!/usr/bin/node
// imports an array and computes a new one
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map(function (x, i) {
  return x * i;
}));
