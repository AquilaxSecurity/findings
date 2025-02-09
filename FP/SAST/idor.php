<?php
session_start();
include_once('./ignore/design/design.php');
$title = 'Secure User Details';
$design = Design(__FILE__, $title);

function secureView($session_token, $username, $user_id) {
    // Use a secure session validation mechanism
    if (!isset($_SESSION['user']) || $_SESSION['user'] !== $username) {
        echo "Unauthorized access.";
        return;
    }

    $allowed_ids = ['1', '2', '3'];
    if (!in_array($user_id, $allowed_ids)) {
        echo "Invalid ID.";
        return;
    }

    $filename = "details/$user_id.json";
    
    if (!file_exists($filename)) {
        echo "User details not found.";
        return;
    }

    echo nl2br(htmlspecialchars(file_get_contents($filename), ENT_QUOTES, 'UTF-8'));
}

if (isset($_COOKIE['user'], $_COOKIE['usess'], $_COOKIE['id'])) {
    $user_id = filter_var($_COOKIE['id'], FILTER_SANITIZE_NUMBER_INT);
    $session_token = preg_replace('/[^a-zA-Z0-9]/', '', $_COOKIE['usess']);
    $username = preg_replace('/[^a-zA-Z0-9]/', '', $_COOKIE['user']);

    echo '<pre style="font-size:16px">';
    secureView($session_token, $username, $user_id);
    echo '</pre>';
} else {
    echo "<p>You must be logged in to view details.</p>";
}

?>

<!DOCTYPE html>
<html>
<head>
    <title><?= htmlspecialchars($title, ENT_QUOTES, 'UTF-8') ?></title>
</head>
<body>
<h1><?= htmlspecialchars($title, ENT_QUOTES, 'UTF-8') ?></h1>
<div>
<?= $design ?>
</div>
</body>
</html>
