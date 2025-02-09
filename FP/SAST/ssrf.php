<?php
function isAllowedURL($url) {
    $allowedDomains = [
        'https://example.com',
        'https://api.example.com'
    ];

    $parsedUrl = parse_url($url);

    if (!$parsedUrl || !isset($parsedUrl['scheme'], $parsedUrl['host'])) {
        return false;
    }

    $fullUrl = $parsedUrl['scheme'] . "://" . $parsedUrl['host'];

    return in_array($fullUrl, $allowedDomains);
}

if (isset($_GET['url'])) {
    $url = filter_var($_GET['url'], FILTER_VALIDATE_URL);
    
    if (!$url || !isAllowedURL($url)) {
        die("Error: Invalid or disallowed URL.");
    }

    $context = stream_context_create([
        'http' => [
            'method' => 'GET',
            'timeout' => 5, 
            'user_agent' => 'SecureApp/1.0'
        ]
    ]);

    $response = @file_get_contents($url, false, $context);

    if ($response === FALSE) {
        die("Error: Unable to fetch the URL.");
    }

    header("Content-Type: text/plain");
    echo htmlspecialchars($response, ENT_QUOTES, 'UTF-8');
} else {
    echo "Please provide a valid 'url' parameter.";
}
?>
