<?php
include_once('./ignore/design/design.php');
$title = 'Secure File Upload';
$design = Design(__FILE__, );

define('UPLOAD_DIR', __DIR__ . '/uploads/');

if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

//validating image file type
function isValidImage($file) {
    $validMimeTypes = ['image/jpeg', 'image/png'];
    $validExtensions = ['jpg', 'jpeg', 'png'];

    $fileMime = mime_content_type($file["tmp_name"]);
    $fileExt = strtolower(pathinfo($file["name"], PATHINFO_EXTENSION));

    return in_array($fileMime, $validMimeTypes) && in_array($fileExt, $validExtensions);
}

function uploadImage($file) {
    if (!isset($file) || !isValidImage($file)) {
        die("Invalid image file!");
    }

    $fileName = uniqid('img_') . '.' . strtolower(pathinfo($file["name"], PATHINFO_EXTENSION));
    $filePath = UPLOAD_DIR . $fileName;

    if (!move_uploaded_file($file["tmp_name"], $filePath)) {
        die("Upload failed!");
    }

    return $filePath;
}

function showImage($imagePath) {
    return base64_encode(file_get_contents($imagePath));
}

if (isset($_POST["submit"])) {
    $imagePath = uploadImage($_FILES["profileImage"]);
    echo "New profile picture has been successfully uploaded!";
} else {
    $imagePath = UPLOAD_DIR . "default.jpg";
}
?>

<html>
<head>
    <title><?= htmlspecialchars($title) ?></title>
</head>
<body>
<h1><?= htmlspecialchars($title) ?></h1>

<img id="profilePicture" src="data:image/png;base64,<?= showImage($imagePath) ?>" alt="Profile Picture">

<div>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="upload">Upload your profile picture! (JPEG/PNG)</label>
        <input type="file" id="profileImage" name="profileImage" required>
        <input type="submit" value="Submit" name="submit">
    </form>
</div>

<div>
    <?= $design ?>
</div>
</body>
</html>
