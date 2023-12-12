#!/usr/bin/node

exports.addMe = (number, theFunction) => {
  theFunction(++number);
};
