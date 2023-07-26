#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersURLs = JSON.parse(body).characters;
    printCharacters(charactersURLs, 0);
  }
});

function printCharacters (charactersURLs, index) {
  request(charactersURLs[index], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < charactersURLs.length) {
        printCharacters(charactersURLs, index + 1);
      }
    }
  });
}
