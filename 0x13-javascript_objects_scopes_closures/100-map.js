#!/usr/bin/node

const list = require('./100-data').list;
const secondList = list.map((element, index) => index * element);

console.log(list);
console.log(secondList);
