#!/usr/bin/node

const values = process.argv.slice(2);
let result = 0;
let trav;
console.log(values);
console.log(values.length);
if (values.length === 0 || values.length === 1) {
  console.log(0);
  throw '';
}

for (trav = 0; trav < values.length; trav++) {
  if (result <= parseInt(values[trav])) {
    result = parseInt(values[trav]);
  }
}

console.log(result);
