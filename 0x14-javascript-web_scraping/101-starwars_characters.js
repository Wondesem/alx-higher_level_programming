#!/usr/bin/node
const request = require('request');
const episodeNumber = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeNumber;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const charDict = {};
    const allChars = JSON.parse(body).characters;
    for (const c in allChars) {
      request(allChars[c], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          charDict[c] = JSON.parse(body).name;
        }
        if (allChars.length === Object.keys(charDict).length) {
          for (const key in charDict) {
            console.log(charDict[key]);
          }
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
