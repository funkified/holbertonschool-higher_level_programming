#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let i = 0;
const newList = list.map(x => x * i++);
console.log(newList);
