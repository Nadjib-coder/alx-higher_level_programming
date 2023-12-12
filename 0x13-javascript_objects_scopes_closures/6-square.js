#!/usr/bin/node

const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let y = 0; y < this.width; y++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}

module.exports = Square;
