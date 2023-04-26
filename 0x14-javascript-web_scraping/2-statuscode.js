#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  process.exit(1);
}

request(url, function (error, response, body) {
  if (!error) {
    console.log('code: ' + response.statusCode);
  }
});
