#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  /* get width () {
    return this._width;
  }
  set width (value) {
    if (value <= 0) {
      return undefined;
    }
    this._width = value;
  }
  get height () {
    return this._height;
  }
  set height (value) {
    if (value <= 0) {
      return undefined;
    }
    this._height = value;
  } */
};
