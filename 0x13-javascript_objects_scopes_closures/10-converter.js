#!/usr/bin/node
// converts a number from base 10 to another base passed as arg
exports.converter = function (base) {
  return function (a) {
    return a.toString(base);
  };
};
