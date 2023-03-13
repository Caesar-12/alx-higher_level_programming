#!/usr/bin/node

function factorial (fac) {
  let value = 1;
  if (fac === 1) {
    return fac;
  }
  value = factorial(fac - 1);
  return fac * value;
}

const num = parseInt(process.argv[2]);

if (!num) {
  console.log(1);
} else {
  const result = factorial(num);
  console.log(result);
}
