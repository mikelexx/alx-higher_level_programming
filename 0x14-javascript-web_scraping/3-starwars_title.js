#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, data) => {
  if (err) {
    console.log(err);
  }
  if (data) {
    console.log(JSON.parse(data).title);
  }
});
