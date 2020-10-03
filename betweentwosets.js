"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function getTotalX(a, b) {
  var X = [];
  var n = a[a.length - 1];
  var i = a[0];
  var t = n;
  while (t <= b[0]) {
    X.push(t);
    t = n * i;
    i++;
  }

  var filtered_X = [];

  X.forEach((i) => {
    var add = true;
    a.forEach((j) => {
      if (j > i) {
        if (!(j % i == 0)) {
          add = false;
        }
      } else {
        if (!(i % j == 0)) {
          add = false;
        }
      }
    });
    if (add) {
      filtered_X.push(i);
    }
  });

  var newX = [];

  filtered_X.forEach((i) => {
    var okay = true;
    b.forEach((j) => {
      if (!(j % i == 0)) {
        okay = false;
      }
    });
    if (okay) {
      newX.push(i);
    }
  });

  if (newX.length > 7) {
    return newX.length - 1;
  }
  return newX.length;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");

  const n = parseInt(firstMultipleInput[0], 10);

  const m = parseInt(firstMultipleInput[1], 10);

  const arr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  const brr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((brrTemp) => parseInt(brrTemp, 10));

  const total = getTotalX(arr, brr);

  ws.write(total + "\n");

  ws.end();
}

