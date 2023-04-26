#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const string = process.argv[3];

if (!fileName || !string) {
  process.exit(1);
}

fs.writeFile(fileName, string, (err) => {
  if (err) {
    process.exit(1);
  }
});
