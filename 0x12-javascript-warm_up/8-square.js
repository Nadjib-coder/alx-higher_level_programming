#!/usr/bin/node

// a script that prints a square

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let y = 0; y < size; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
