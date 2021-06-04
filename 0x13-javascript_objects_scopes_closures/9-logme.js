#!/usr/bin/node
// prints the number of args already printed and the new arg value
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
