#!/usr/bin/node

const sqSize = parseInt(process.argv[2], 10);
if (isNaN(sqSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqSize; i++) {
    console.log('X'.repeat(sqSize));
  }
}
