#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    return num.tostring(base);
  };
};
