#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < height; i++) {
      let rec = '';
      for (let y = 0; y < width; y++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}

module.exports = Rectangle;
