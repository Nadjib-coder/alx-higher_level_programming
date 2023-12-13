#!/usr/bin/node

const file = require('file');
const firstArg = file.readFileSync(process.argv[2]).toString();
const secondArg = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], firstArg + secondArg);
