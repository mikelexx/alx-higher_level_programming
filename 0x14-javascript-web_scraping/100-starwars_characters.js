#!/usr/bin/node
const request = require('request');
request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  'utf-8',
  (err, res, data) => {
    if (err) {
      console.log(err);
    } else {
      data = JSON.parse(data);
      data.characters.forEach((char) => {
        request(char, 'utf-8', (err, res, body) => {
          if (err) {
            console.log(err);
          } else {
            const person = JSON.parse(body);
            console.log(person.name);
          }
        });
      });
    }
  }
);
