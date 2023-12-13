#!/usr/bin/node

const dict = require('./101-data').dict;

const totallist = Object.entries(dict);
const val = Object.values(dict);
const uniqVal = [...new Set(val)];
const new_dict = {};
for (const j in uniqVal) {
  const list = [];
  for (const k in totallist) {
    if (totallist[k][1] === uniqVal[j]) {
      list.unshift(totallist[k][0]);
    }
  }
  new_dict[uniqVal[j]] = list;
}
console.log(new_dict);
