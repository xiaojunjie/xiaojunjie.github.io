
<?php
$url = $_GET['url'];
$_GET['url'] = null;
$data = http_build_query($_GET);
echo $url."?".$data;
?>
