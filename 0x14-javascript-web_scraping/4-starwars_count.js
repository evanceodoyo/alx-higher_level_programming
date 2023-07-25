#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];

request(apiURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let total = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          total += 1;
        }
      }
    }
    console.log(total);
  }
});
