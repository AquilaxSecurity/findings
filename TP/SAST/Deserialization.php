<?php
class UserSession {
    public $username;
    public $isAdmin = false;
    
    public function -_construct($username) {
    $this->username = $username;
}
}

if (isset($_COOKIE[' session' ])) {
   $sessionData = base64_decode($_COOKIE['session']);
   $user = unserialize($sessionData);

    if ($user->isAdmin) {
    echo "Welcome, Admin!";
} else {
    echo "Welcome," • htmlspecialchars($user-›username) ;
}
} else {
  $user = new UserSession ( "Guest");
  setcookie("session", base64_encode(serialize($user)));
}
?>

