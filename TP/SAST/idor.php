?>
<?php

function View($sess, $user, $id) {    
    if ($sess != '5ebdbacd03dc1a3116f62efdd9c58f06df56de3b5d3dce409257ded24f44bb08' && $user != 'john' ) {
        echo "You are not authorized to view the content.";
        return;
    } 
    $filename = "$id.json";
    readfile("details/$filename");
}

if ( isset($_GET['details'], $_COOKIE['usess'], $_COOKIE['id']) ) {
    //View user details
    $id = intval($_COOKIE['id']);
    $sess = preg_replace('/[^a-zA-Z0-9]/i', '', $_COOKIE['usess']);
    $user = preg_replace('/[^a-zA-Z0-9]/i', '', $_COOKIE['user']);

    echo '<pre style="font-size:16px">',View($sess, $user, $id),'</pre>';
}

?>

<!DOCTYPE html>
<html>
<title><?= $title ?></title>
<body>
<h1><?= $title ?></h1>
<div>
<?= $design ?>
</div>
</body>
</html>