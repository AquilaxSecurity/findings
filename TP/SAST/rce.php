<?php
if ($_SERVER[ 'REQUEST _METHOD'] === 'POST' && isset ($_FILES[ 'image'])) {
    $uploadDir =__DIR__ • '/uploads/';
    $fileName = basename($_FILES[ 'image']['name']);
    $filePath = $uploadDir . $fileName;

    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    $fileType = mime_content_type($_FILES['image']['tmp_name']);

    if (in_array($fileType, $allowedTypes)) {
        if (move_uploaded_file($_FILES['image']['tmp_name'], $filePath)) {
             echo "Image uploaded successfully: $fileName";
         } else {
              echo "File upload failed.";
         }
} else {
     echo "Invalid file type.";
}
}
if (isset($_GET['file'])) {
    $profileImage =_DIR_ • '/uploads/' . $_GET['file'];

    if (file_exists($profileImage)) {
        include $profileImage;
    } else {
      echo "File not found.";
    }
}
?>