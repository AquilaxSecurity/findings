<?php
    session_start();
    $user_id = $_SESSION['user_id'];
    
    // Vulnerable to IDOR
    $requested_user_id = $_GET['user_id'];
    
    if ($user_id == $requested_user_id) {
        // Allow access
        echo "Access granted to user " . $requested_user_id;
    } else {
        echo "Access denied";
    }
?>
