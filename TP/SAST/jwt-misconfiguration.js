const express = require("express");
const jwt = require("jsonwebtoken");

const app = express();
app.use(express.json());

const SECRET_KEY = "mysecret";

app.post("/login", (req, res) => {
    const { username } = req.body;
    const token = jwt.sign({ username: username, role: "user" }, SECRET_KEY, { algorithm: "none" });
    res.json({ token });
});

app.get("/admin", (req, res) => {
    const token = req.headers.authorization?.split(" ")[1];
    if (!token) {
        return res.status(401).json({ error: "Token required" });
    }

    const decoded = jwt.decode(token); 

    if (decoded.role === "admin") {
        return res.json({ message: "Welcome, Admin!" });
    } else {
        return res.status(403).json({ error: "Access denied" });
    }
});

app.listen(3000, () => console.log("Server running on port 3000"));
