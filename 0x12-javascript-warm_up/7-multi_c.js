#!/usr/bin/node

const count = parseInt(process.argv[2]);
let i;

if (!count) {
  console.log('Missing number of occurrences');
}

for (i = 0; i < count; i++) {
  console.log('C is fun');
}
