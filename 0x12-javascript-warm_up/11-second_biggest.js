#!/usr/bin/node
// prints the second biggest int of the argument list, or 0
const args = process.argv;
let min1;
let min2;
for (let x = 2; args[x]; x++) {
  const val = parseInt(args[x]);
  if (!min1) {
    min1 = val;
  } else if (!min2) {
    min2 = val;
  }
  if (val < min1) {
    min2 = min1;
    min1 = val;
  } else if (val < min2) {
    min2 = val;
  }
}
console.log(min2 || '0');
