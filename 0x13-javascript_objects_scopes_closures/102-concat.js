#!/usr/bin/node

const files = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fArg + sArg);
