#!/usr/bin/node
/*
prints a formatted string with first argument converted to int, or
"Not a number" if not
*/
const val = parseInt(process.argv[2]);
if (val) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
