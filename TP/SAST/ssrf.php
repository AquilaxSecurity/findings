<?php
if (isset($_GET['url'])) {
    $url = $_GET['url'];

    $response = file_get_contents($url);
    echo $response;
} else {
    echo "Please provide a 'url' parameter.";
}
?>