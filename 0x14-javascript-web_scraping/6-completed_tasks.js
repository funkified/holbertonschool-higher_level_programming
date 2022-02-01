#!/usr/bin/node
const request = require('request');
const tasks = {};
request(process.argv[2], function (err, request, body) {
  if (err) {
    console.log(err);
  }
  for (const user of JSON.parse(body)) {
    if (user.completed === true) {
      if (tasks[user.userId] === undefined) {
        tasks[user.userId] = 0;
      }
      tasks[user.userId]++;
    }
  }
  console.log(tasks);
});
