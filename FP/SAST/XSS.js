const express = require('express');
const app = express();
const escape = require('escape-html');

app.get('/search', (req, res) => {
  let searchTerm = req.query.term || '';

  const safeSearchTerm = escape(searchTerm);

  res.send(`<h1>Search results for: ${safeSearchTerm}</h1>`);
});

app.listen(3000, () => console.log('App running on port 3000'));
