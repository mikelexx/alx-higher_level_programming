#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, 'utf-8', (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, data, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
