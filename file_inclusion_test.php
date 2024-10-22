<?php
    $file = $_GET['file'];
    
    // Vulnerable to File Inclusion
    include($file);
?>
