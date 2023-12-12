#!/usr/bin/node

exports.exec = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
