<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $xml_data = file_get_contents("php://input");

    $dom = new DOMDocument();
    libxml_disable_entity_loader(true);
    
    $dom->loadXML($xml_data, LIBXML_NOENT | LIBXML_DTDLOAD | LIBXML_DTDATTR | LIBXML_NOERROR | LIBXML_NOWARNING);

    $username = $dom->getElementsByTagName("username")->item(0)->nodeValue;
    echo "Hello, " . htmlspecialchars($username);
}
?>
