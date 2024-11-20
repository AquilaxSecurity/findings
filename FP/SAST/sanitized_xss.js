const express = require('express');
const app = express();

app.get('/', (req, res) => {
  const name = req.query.name;
  const sanitized = name.replace(/</g, "&lt;").replace(/>/g, "&gt;");
  res.send(`<h1>Hello ${sanitized}</h1>`);
});

app.listen(3000);
