#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.
const numberOfArguments = process.argv.length - 2;

if (numberOfArguments === 0 || numberOfArguments === 1) {
  console.log(0);
} else {
  const array = process.argv.slice(2).map(Number);
  const second = array.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
