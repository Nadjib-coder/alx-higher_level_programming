#!/usr/bin/node

let numberOfArguments = 0;
exports.logMe = function (item) {
  console.log(numberOfArguments + ': ' + item);
  numberOfArguments++;
};
