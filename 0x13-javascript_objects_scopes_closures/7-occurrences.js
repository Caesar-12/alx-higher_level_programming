#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occured = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occured += 1;
    }
  }
  return occured;
};
