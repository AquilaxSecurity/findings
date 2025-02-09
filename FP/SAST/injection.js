const db = require('./ignore/db/db.js');
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const bcrypt = require('bcrypt');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/login.html'));
});

app.post('/', async function (req, res) {
    try {
        const username = req.body.username;
        const password = req.body.password;

        if (!username || !password) {
            return res.status(400).send("Invalid input.");
        }

        const [rows] = await db.execute(`SELECT password FROM users WHERE username = ?`, [username]);

        if (rows.length === 0) {
            return res.status(401).send("Invalid username or password"); 
        }

        const storedHashedPassword = rows[0].password;

        const passwordMatch = await bcrypt.compare(password, storedHashedPassword);

        if (!passwordMatch) {
            return res.status(401).send("Invalid username or password"); // Generic error
        }

        return res.send("Logged in successfully!");

    } catch (err) {
        console.error('Error executing query:', err);
        return res.status(500).send("Internal Server Error");
    }
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
