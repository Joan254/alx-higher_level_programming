#!/usr/bin/node
const PrevSquare = require('./5-square');
class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let j = 0;
      while (j < this.width) {
        myVar += myChar;
        j++;
      }
      console.log(myVar);
    }
  }
}
module.exports = Square;
