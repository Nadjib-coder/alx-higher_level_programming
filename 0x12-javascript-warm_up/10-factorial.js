#!/usr/bin/node

// a script that computes and prints a factorial

const num1 = parseInt(process.argv[2]);

function factorial (num) {
  return num * factorial(num - 1);
}

const result = factorial(num1);
console.log(result);
