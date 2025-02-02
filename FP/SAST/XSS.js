const express = require('express');
const app = express();
const escape = require('lodash.escape');

app.get('/search', (req, res) => {
  let searchTerm = req.query.term || '';

  searchTerm = escape(searchTerm);

  res.send(`<h1>Search results for: ${searchTerm}</h1>`);
});
