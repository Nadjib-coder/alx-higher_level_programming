#!/usr/bin/node

const dict = require('./101-data').dict;
const userOccurrences = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (occurrence in userOccurrences) {
    userOccurrences[occurrence].push(userId);
  } else {
    userOccurrences[occurrence] = [userId];
  }
}
console.log(userOccurrences);
