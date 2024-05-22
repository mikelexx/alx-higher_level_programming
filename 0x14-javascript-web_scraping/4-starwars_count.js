#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/', (err, res, data) => {
  if (err) {
    console.log(err);
  }
  if (data) {
    let count = 0;
    JSON.parse(data).results.forEach(movie => {
      movie.characters.forEach(char => {
        if (char === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      });
    });
    console.log(count);
  }
});
