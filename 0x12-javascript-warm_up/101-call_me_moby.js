#!/usr/bin/node

exports.callMe = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
