#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  return list.reduce(function (count, currentElement) {
    if (currentElement === searchElement) {
      count++;
    }
  return (count);
  }, 0);
};
