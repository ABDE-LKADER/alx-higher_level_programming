#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  return list.reduce(function (count, currentElement) {
    if (currentElement === searchElement) {
      count++;
    }
  return (count);
  });
};
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));
