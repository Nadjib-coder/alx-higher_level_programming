#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1Path, file2Path, destinationPath) {
  const file1Content = fs.readFileSync(file1Path, 'utf-8');
  const file2Content = fs.readFileSync(file2Path, 'utf-8');
  const concatenatedContent = file1Content + file2Content;
  fs.writeFileSync(destinationPath, concatenatedContent, 'utf-8');
}

const [,, file1Path, file2Path, destinationPath] = process.argv;

concatFiles(file1Path, file2Path, destinationPath);
