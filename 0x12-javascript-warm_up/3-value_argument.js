#!/usr/bin/node
// prints first argument passed
const msg = process.argv[2];
msg ? console.log(msg) : console.log('No argument');
