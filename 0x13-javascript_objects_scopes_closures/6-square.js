#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
