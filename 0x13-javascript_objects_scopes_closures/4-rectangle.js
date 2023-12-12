#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let rec = '';
      for (let j = 0; j < this.height; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
