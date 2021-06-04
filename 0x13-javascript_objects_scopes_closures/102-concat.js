#!/usr/bin/node
// concats 2 files, passed as 1st and 2nd arg, into file at 3rd arg
const fs = require('fs');
let data = fs.readFileSync(process.argv[2]).toString();
data += fs.readFileSync(process.argv[3]).toString();
fs.writeFile(process.argv[4], data, function (err) {
  if (err) {
    return console.error(err);
  }
});
