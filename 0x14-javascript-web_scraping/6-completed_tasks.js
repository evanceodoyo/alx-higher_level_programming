#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedObj = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (task.userId in completedObj) {
          completedObj[task.userId] += 1;
        } else {
          completedObj[task.userId] = 1;
        }
      }
    }
    console.log(completedObj);
  }
});
