#!/usr/bin/node

exports.callMe = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
