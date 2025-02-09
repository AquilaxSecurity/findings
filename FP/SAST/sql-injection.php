<?php
session_start();
$conn = new mysqli("localhost", "root", "mydb");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    if (empty($username) || empty($password)) {
        die("Error: Username and password are required.");
    }
    $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    
    if ($stmt->num_rows === 0) {
        echo "Invalid username or password"; 
    } else {
        $stmt->bind_result($hashed_password);
        $stmt->fetch();

        // Verify password securely
        if (password_verify($password, $hashed_password)) {
            $_SESSION['username'] = $username;
            echo "Login successful!";
        } else {
            echo "Invalid username or password";
        }
    }

    $stmt->close();
    $conn->close();
}
?>
