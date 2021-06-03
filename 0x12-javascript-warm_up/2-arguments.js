#!/usr/bin/node
// prints a message dependent on number of arguments given
const lines = process.argv.length;
if (lines === 0) {
  console.log('No argument');
} else if (lines === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
