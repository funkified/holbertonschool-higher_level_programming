#!/usr/bin/node
const str = parseInt(process.argv[2]);
if (isNaN(str)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < str; i++) { console.log('C is fun'); }
}
