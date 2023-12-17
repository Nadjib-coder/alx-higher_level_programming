#!/usr/bin/node

const fs = require('fs');

exports.concats = function (file1Path, file2Path, destinationPath) {
  const file1Content = fs.readFileSync(file1Path, 'utf-8');
  const file2Content = fs.readFileSync(file2Path, 'utf-8');
  const concatenatedContent = file1Content + file2Content;
  fs.writeFileSync(destinationPath, concatenatedContent, 'utf-8');
};
