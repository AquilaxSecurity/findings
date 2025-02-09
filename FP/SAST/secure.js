const express = require('express');
const axios = require('axios');
const { URL } = require('url');
const dns = require('dns').promises;

const app = express();

const ALLOWED_DOMAINS = ['example.com', 'api.example.com'];

async function isAllowedURL(userURL) {
    try {
        const parsedURL = new URL(userURL);
        const hostname = parsedURL.hostname;

        const ips = await dns.lookup(hostname);
        
        // Only allow known domains (whitelist)
        if (!ALLOWED_DOMAINS.includes(hostname)) {
            return false;
        }

        return true;
    } catch (error) {
        return false;
    }
}

app.get('/profile', (req, res) => {
    console.log('Received request for /profile');

    const profileData = {
        name: 'John Doe',
        role: 'Developer'
    };

    res.json(profileData);
    console.log('Sent profile data response');
});

app.get('/fetch-data', async (req, res) => {
    const url = req.query.url;
    console.log(`Received request for /fetch-data with URL: ${url}`);

    if (!url) {
        return res.status(400).send('Missing URL parameter');
    }

    // Validate the URL against the whitelist
    if (!(await isAllowedURL(url))) {
        console.warn(`Blocked SSRF attempt: ${url}`);
        return res.status(403).send('Forbidden: Invalid URL');
    }

    try {
        const response = await axios.get(url, { timeout: 5000 });
        res.send(response.data);
        console.log(`Data fetched and sent for URL: ${url}`);
    } catch (error) {
        console.error(`Error fetching data from URL: ${url}`, error);
        res.status(500).send('Error fetching data');
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
