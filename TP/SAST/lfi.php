<?php
#Retrieves a value from the file in the URL and assigns it to the $data variable. Injecting malicious input in the file paramater, this can lead to LFI.
$data = $_GET['file'];
 # It loads the file specified in the file parameter.
include($data);
?>
