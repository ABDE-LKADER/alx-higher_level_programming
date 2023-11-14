#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super (size, size);
  }
};

const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
