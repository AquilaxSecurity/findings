<?php

$allowed_files = [
    "home" => "pages/home.php",
    "contact" => "pages/contact.php",
    "about" => "pages/about.php"
];

if (isset($_GET['file'])) {
    $file = $_GET['file'];

    if (array_key_exists($file, $allowed_files)) {
        include($allowed_files[$file]);
    } else {
        die("Access Denied: Invalid file.");
    }
} else {
    include("pages/home.php");
}
?>
