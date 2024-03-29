#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];

if (!fileName) {
  process.exit(1);
}

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  console.log(data);
});
