#!/usr/bin/node
// returns the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      num++;
    }
  }
  return num;
};
