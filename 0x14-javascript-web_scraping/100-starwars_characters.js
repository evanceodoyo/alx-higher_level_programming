#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersURLs = JSON.parse(body).characters;
    for (const characterURL of charactersURLs) {
      request(characterURL, function (error, response, body) {
        console.log(JSON.parse(body).name);
      });
    }
  }
});
