<?php
include 'flag.php';
$encodeFlag = base64_encode($flag);
// 响应头添加flag
header("X-flag:".$encodeFlag);
phpinfo();

