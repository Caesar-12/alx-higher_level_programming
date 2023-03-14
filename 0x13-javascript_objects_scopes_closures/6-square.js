#!/usr/bin/node

const Squarepar = require('./5-square');

module.exports = class Square extends Squarepar {
  constructor (size) {
    super();
    this.size = size;
    /* console.log(this.size); */
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
