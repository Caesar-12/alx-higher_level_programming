#!/usr/bin/node

const fs = require('fs');
const file_name = process.argv[2];

if (!file_name) {
	process.exit(1);
}

fs.readFile(file_name, 'utf8', (err, data) => {
if (err) {
	console.error(err);
	process.exit(1);
}

console.log(data);
});

