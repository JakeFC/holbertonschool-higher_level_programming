#!/usr/bin/node
// prints first argument passed, or 'No argument' if none
const msg = process.argv[2];
msg ? console.log(msg) : console.log('No argument');
