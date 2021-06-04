#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data.js').dict;
const dict2 = {};
for (const value of Object.values(dict)) {
  dict2[value] = [];
}
for (const key of Object.keys(dict)) {
  dict2[dict[key]].push(key);
}
console.log(dict2);
