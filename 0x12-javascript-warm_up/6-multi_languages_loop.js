#!/usr/bin/node
/*
prints 3 lines using an array of a string and a loop
*/
const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let idx = 0;
for (idx in array) {
  console.log(array[idx]);
}
