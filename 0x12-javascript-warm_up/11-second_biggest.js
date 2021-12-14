#!/usr/bin/node
let secBig = 0;
const num = process.argv.slice(2);
if (num.length > 1) {
  num.sort();
  secBig = num[num.length - 2];
}
console.log(secBig);
