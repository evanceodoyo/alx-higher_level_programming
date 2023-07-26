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
      if (task.completed && !completedObj[task.userId]) {
        completedObj[task.userId] = 0;
      }
      if (task.completed) {
        completedObj[task.userId] += 1;
      }
    }
    console.log(completedObj);
  }
});
