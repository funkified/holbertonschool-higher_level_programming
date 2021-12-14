#!/usr/bin/node
exports.esrever = function (list) {
  let lst = [];

  for (let i = list.length; i >= 0; i--) {
    lst.push(list[i]);
  }
  lst = lst.slice(1);
  return lst;
};
