<?php
class UserSession {
    public $username;
    public $isAdmin = false;

    public function __construct($username) {
        $this->username = $username;
    }
}

session_start();

if (isset($_COOKIE['session'])) {
    $sessionData = json_decode(base64_decode($_COOKIE['session']), true);

    if (is_array($sessionData) && isset($sessionData['username'], $sessionData['isAdmin'])) {
        $user = new UserSession(htmlspecialchars($sessionData['username']));
        $user->isAdmin = (bool)$sessionData['isAdmin'];
    } else {
        $user = new UserSession("Guest");
    }
} else {
    $user = new UserSession("Guest");
}

$sessionJson = base64_encode(json_encode([
    'username' => $user->username,
    'isAdmin' => $user->isAdmin
]));

setcookie("session", $sessionJson, [
    'expires' => time() + 3600, 
    'path' => '/',
    'secure' => true,  
    'httponly' => true, 
    'samesite' => 'Strict'
]);

if ($user->isAdmin) {
    echo "Welcome, Admin!";
} else {
    echo "Welcome, " . htmlspecialchars($user->username, ENT_QUOTES, 'UTF-8');
}
?>
