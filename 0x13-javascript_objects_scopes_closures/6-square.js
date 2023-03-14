#!/usr/bin/node

const Squarepar = require('./5-square');

module.exports = class Square extends Squarepar {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
