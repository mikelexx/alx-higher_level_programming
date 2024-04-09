#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(el => {
    if (el === searchElement) {
      counter++;
    }
  });
  return counter;
};
