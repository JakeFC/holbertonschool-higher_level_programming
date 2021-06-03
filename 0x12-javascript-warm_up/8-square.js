#!/usr/bin/node
// prints a square of X's the size of first argument, else "Missing size"
const num = parseInt(process.argv[2]);
if (num !== null) {
  for (let y = 0; y < num; y++) {
    for (let x = 0; x < num; x++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
