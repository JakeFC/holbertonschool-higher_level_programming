#!/usr/bin/node
// prints the second biggest int of the argument list, or 0
const args = process.argv;
let max1;
let max2;
for (let x = 2; args[x]; x++) {
  const val = parseInt(args[x]);
  if (!max1) {
    max1 = val;
  } else if (!max2) {
    if (val > max1) {
      max2 = max1;
      max1 = val;
    } else {
      max2 = val;
    }
  }
  if (val > max1) {
    max2 = max1;
    max1 = val;
  } else if (val > max2) {
    max2 = val;
  }
}
console.log(max2 || '0');
