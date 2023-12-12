#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let y = 0; y < this.width; y++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}

module.exports = Rectangle;
