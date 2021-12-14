#!/usr/bin/node

exports.converter = function (base) {
  return function (Convert) {
    return Convert.toString(base);
  };
};
