const express = require("express");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");

const app = express();
app.use(express.json());

const SECRET_KEY = crypto.randomBytes(64).toString("hex");

app.post("/login", (req, res) => {
    const { username } = req.body;
    const token = jwt.sign({ username: username, role: "user" }, SECRET_KEY, { algorithm: "HS256", expiresIn: "1h" });
    res.json({ token });
});

function authenticateToken(req, res, next) {
    const token = req.headers.authorization?.split(" ")[1];
    if (!token) {
        return res.status(401).json({ error: "Token required" });
    }

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        req.user = decoded;
        next();
    } catch (error) {
        return res.status(403).json({ error: "Invalid Token" });
    }
}

app.get("/admin", authenticateToken, (req, res) => {
    if (req.user.role !== "admin") {
        return res.status(403).json({ error: "Access denied" });
    }
    return res.json({ message: "Welcome, Admin!" });
});

app.listen(3000, () => console.log("Server running on port 3000"));
