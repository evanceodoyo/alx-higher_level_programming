#!/usr/bin/node

const sqSize = parseInt(process.argv[2], 10);
if (isNaN(sqSize)) {
  console.log('Missing size');
} else {
  let sqString = 'X'.repeat(sqSize);
  for (let i = 0; i < sqSize; i++) {
    console.log(sqString);
  }
}
