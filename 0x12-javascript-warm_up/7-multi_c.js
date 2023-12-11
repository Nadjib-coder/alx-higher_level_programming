#!/usr/bin/node

let numberOfArguments = parseInt(process.argv[2]);

if (isNaN(numberOfArguments)) {
  console.log('Missing number of occurrences');
} else {
  while (numberOfArguments > 0) {
    console.log('C is fun');
    numberOfArguments--;
  }
}
