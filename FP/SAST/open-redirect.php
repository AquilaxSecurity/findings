<?php

function isValidRedirect($url) {
 
    $allowlist = [
        "https://www.example.com/login.php",
        "https://www.example.com/logout.html",
        "https://www.example.com/dashboard"
    ];

    return in_array($url, $allowlist, true);
}

if (isset($_GET['logout'])) {

    ob_start();

    $url = "https://www.example.com/login.php";

    if (isset($_GET['redirect_to']) && isValidRedirect($_GET['redirect_to'])) {
        $url = $_GET['redirect_to'];
    }

    header("Location: " . htmlspecialchars($url, ENT_QUOTES, 'UTF-8'), true, 303);
    exit;
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
