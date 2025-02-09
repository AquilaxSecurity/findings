<?php
class User {
    private int $id;
    private string $username;
    private string $note;
    private mysqli $db;

    function __construct(mysqli $db, int $id, string $username, string $note = '') {
        $this->id =  $id;
        $this->username =  $username;
        $this->note = $note;
        $this->db = $db;
    }

    function new_note(): void {
        if (!empty($this->note)) {
            $stmt = $this->db->prepare("UPDATE users SET note = ? WHERE username = ? AND id = ?");
            $stmt->bind_param("ssi", $this->note, $this->username, $this->id);
            $stmt->execute();
            $stmt->close();
        }
    }

    function share_notes(): void {
        $stmt = $this->db->prepare("SELECT note FROM users WHERE username = ? AND id = ?");
        $stmt->bind_param("si", $this->username, $this->id);
        $stmt->execute();
        $stmt->bind_result($value);
        $stmt->fetch();
        $stmt->close();

        if (!empty($value)) {
            $stmt = $this->db->prepare("SELECT username, note FROM users WHERE note = ?");
            $stmt->bind_param("s", $value);
            $stmt->execute();
            $result = $stmt->get_result();

            while ($row = $result->fetch_assoc()) {
                echo "<h4>[+] " . htmlspecialchars($row['username']) . ": " . htmlspecialchars($row['note']) . "</h4>";
            }
            $stmt->close();
        }
    }
}

function user_validated(): bool {
    return true;
}

$mysqlDB = new mysqli("localhost", "secure_user", "strong_password", "secure_db");

if ($mysqlDB->connect_error) {
    die("Database connection failed: " . $mysqlDB->connect_error);
}

if (user_validated()) {
    $current_user = new User($mysqlDB, 1, 'Mario');

    if (isset($_GET['note'])) {
        $current_user->note = filter_input(INPUT_GET, 'note', FILTER_SANITIZE_STRING);
        $current_user->new_note();
    }

    if (isset($_GET['view']) && !isset($_GET['note'])) {
        $current_user->share_notes();
    }
}
?>
