<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
    $uploadDir = __DIR__ . '/uploads/';
    $fileName = basename($_FILES['image']['name']);
    $filePath = $uploadDir . $fileName;

    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    $fileType = mime_content_type($_FILES['image']['tmp_name']);

    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    $allowedExts = ['jpg', 'jpeg', 'png', 'gif'];

    if (in_array($fileType, $allowedTypes) && in_array($fileExt, $allowedExts)) {
        $newFileName = uniqid() . "." . $fileExt;
        $newFilePath = $uploadDir . $newFileName;

        if (move_uploaded_file($_FILES['image']['tmp_name'], $newFilePath)) {
            echo "Image uploaded successfully: $newFileName";
        } else {
            echo "File upload failed.";
        }
    } else {
        echo "Invalid file type.";
    }
}

if (isset($_GET['file'])) {
    $fileName = basename($_GET['file']);
    $profileImage = __DIR__ . '/uploads/' . $fileName;

    if (pathinfo($fileName, PATHINFO_EXTENSION) !== "jpg" &&
        pathinfo($fileName, PATHINFO_EXTENSION) !== "jpeg" &&
        pathinfo($fileName, PATHINFO_EXTENSION) !== "png" &&
        pathinfo($fileName, PATHINFO_EXTENSION) !== "gif") {
        die("Invalid file format.");
    }

    if (file_exists($profileImage) && is_readable($profileImage)) {
        header("Content-Type: " . mime_content_type($profileImage));
        readfile($profileImage);
    } else {
        echo "File not found.";
    }
}
?>
