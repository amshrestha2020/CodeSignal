This is a simple console application that is meant to print numbers from 1 to 100, but replacing any lucky number with the word "Lucky!" A lucky number is defined as a number that is either divisible by 7 or that contains the digit 7.

Take a look at luckyNumberPrinter.js to see the overall logic of the application, then look at luckyChecker.js for the isLucky function. Fill in the missing implementation for isLucky so that the application prints the expected output.

The first twenty rows of output should look like this:

1
2
3
4
5
6
Lucky!
8
9
10
11
12
13
Lucky!
15
16
Lucky!
18
19
20



// LuckyChecker.js
/**
 * A number is lucky when it is divisible by 7 or when it contains a 7.
 */
const isLucky = (x) => {
    // TODO
    return x % 7 === 0 || x.toString().includes('7');
  };
  
  module.exports = {
      isLucky,
  };


// LuckyNumberPrinter.js
const { isLucky } = require('./luckyChecker.js');

for (let i = 1; i <= 100; i++) {
    if (isLucky(i)) {
        console.log(`Lucky!`)
    } else {
        console.log(i);
    }
}
