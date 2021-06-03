#!/usr/bin/node
/*
prints "C is fun" x times, where x is the first argument, if it converts to
int, else prints "missing number of occurences"
*/
const num = parseInt(process.argv[2]);
if (num || num === 0) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
