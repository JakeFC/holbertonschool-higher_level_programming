#!/usr/bin/node
// replaces myObject attribute named "value" with another value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
