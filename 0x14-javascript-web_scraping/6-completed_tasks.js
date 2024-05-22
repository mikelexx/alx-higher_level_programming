#!/usr/bin/node
const request = require('request');
const userTodos = {};
request(process.argv[2], 'utf-8', (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    data = JSON.parse(data);
    data.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (typeof userTodos[userId] === 'undefined') {
          userTodos[userId] = 1;
        } else {
          userTodos[userId]++;
        }
      }
    });
    console.log(userTodos);
  }
});
