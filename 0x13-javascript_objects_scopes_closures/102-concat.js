#!/usr/bin/node

const files = require('files');

const firstArg = files.readFileSync(process.argv[2]).toString();
const secondArg = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], firstArg + secondArg);
