#!/usr/bin/node

const values = process.argv.slice(2);
let result = 0;

if (values.length === 0 || values.length === 1) {
  console.log(0);
} else {
  values.sort(function (a, b) { return b - a; });
  result = values[1];
  console.log(result);
}
