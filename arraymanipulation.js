"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map((str) => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the arrayManipulation function below.
function arrayManipulation(n, queries) {
  var arr = [];

  for (let i = 0; i < n; i++) {
    let t = 0;
    arr.push(t);
  }

  for (let i = 0; i < queries.length; i++) {
    for (let j = queries[i][0]; j <= queries[i][1]; j++) {
      arr[j - 1] += queries[i][2];
    }
  }

  var max = arr[0];

  arr.forEach((i) => {
    if (i > max) {
      max = i;
    }
  });

  return max;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const nm = readLine().split(" ");

  const n = parseInt(nm[0], 10);

  const m = parseInt(nm[1], 10);

  let queries = Array(m);

  for (let i = 0; i < m; i++) {
    queries[i] = readLine()
      .split(" ")
      .map((queriesTemp) => parseInt(queriesTemp, 10));
  }

  let result = arrayManipulation(n, queries);

  ws.write(result + "\n");

  ws.end();
}
