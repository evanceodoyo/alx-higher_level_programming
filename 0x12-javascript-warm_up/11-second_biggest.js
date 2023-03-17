#!/usr/bin/node

const argsArray = process.argv.slice(2);
function secondLarge (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((a, b) => a - b);
    arr.pop();
    return (arr.pop());
  }
}
console.log(secondLarge(argsArray));
