<?php

$ALLOWED_DOMAINS = ['example.com', 'trusted-domain.com'];

if (isset($_GET['url'])) {
    $url = $_GET['url'];

    $parsed_url = parse_url($url);
    $host = $parsed_url['host'] ?? '';

    if (in_array($host, $ALLOWED_DOMAINS)) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);

        echo $response;
    } else {
        echo "Access to the provided URL is not allowed.";
    }
} else {
    echo "Please provide a 'url' parameter.";
}
?>