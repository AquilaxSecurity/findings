<?php
include_once('./ignore/design/design.php');
$title = 'Denial-of-service';
$design = Design(__FILE__, $title);

function InviteLink($from, $to) {

    $f = filter_var($from, FILTER_VALIDATE_INT, ["options" => ["min_range" => 0, "max_range" => 16]]);
    $t = filter_var($to, FILTER_VALIDATE_INT, ["options" => ["min_range" => $f, "max_range" => 64]]);

    if ($f === false || $t === false || $f >= $t) {
        return null;
    }

    $length = $t - $f;
    $randomBytes = random_bytes(ceil($length / 2));
    $invite = substr(bin2hex($randomBytes), 0, $length);

    $link = "https://" . htmlspecialchars($_SERVER['SERVER_NAME']) . "/" . $invite;

    return $link;
}

?>

<!DOCTYPE html>
<html>
<head>
    <title><?= htmlspecialchars($title) ?></title>
</head>
<body>
<h1><?= htmlspecialchars($title) ?></h1>
<div>
    <?= $design ?>
</div>

<h2>Generate an invite link</h2>

<?php
$from = filter_input(INPUT_GET, 'from', FILTER_SANITIZE_NUMBER_INT);
$to = filter_input(INPUT_GET, 'to', FILTER_SANITIZE_NUMBER_INT);

if ($from !== null && $to !== null) {
    $link = InviteLink($from, $to);
    if ($link !== null) {
        echo "<p>Your link: <a href=\"" . htmlspecialchars($link) . "\">" . htmlspecialchars($link) . "</a></p>";
    } else {
        echo "<p>Invalid input. Please ensure 'from' is between 0-16 and 'to' is between 'from'-64.</p>";
    }
}
?>

</body>
</html>
