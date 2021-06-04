#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  const revs = [];
  for (let i = 0; list[i]; i++) {
    revs.unshift(list[i]);
  }
  return revs;
};
