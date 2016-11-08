<?php
global $tapatalk_log;
include(MBQ_3RD_LIB_PATH .'KLogger.php');
$errorLog = MBQ_PATH . 'log';
if(!empty($errorLog) && is_writable($errorLog) && class_exists('KLogger'))
{
    $tapatalk_log = new KLogger($errorLog, KLogger::INFO);
    if(MBQ_DEBUG)
    {
        $old_error_handler = set_error_handler("TT_ErrorHandler", MBQ_DEBUG);
    }
}
function TT_ErrorHandler($errno, $errstr, $errfile, $errline)
{
    global $tapatalk_log, $old_error_handler;
    $error_string 	= "[" . date("d-M-Y H:i:s", $_SERVER['REQUEST_TIME']) . '] PHP ' . $errno . '::' . $errstr . " in " . $errfile . " on line " . $errline . PHP_EOL;
    switch ($errno) {
        case E_ERROR:
        case E_USER_ERROR:
            $tapatalk_log->logError($error_string);
            break;
        case E_WARNING:
        case E_USER_WARNING:
            $tapatalk_log->logWarn($error_string);
            break;
        case E_NOTICE:
        case E_USER_NOTICE:
            $tapatalk_log->logNotice($error_string);
            break;
        
        default:
            $tapatalk_log->logInfo($error_string);
            break;
    }
    if(MBQ_DEBUG)
    {
        restore_error_handler();
        return false;
    }
    return true;
}
function TT_LogException(Exception $ex)
{
    global $tapatalk_log;
    if(is_a($tapatalk_log, 'KLogger'))
    {
        TT_ErrorHandler($ex->getCode(), $ex->getMessage() . PHP_EOL . $ex->getTraceAsString() . PHP_EOL . PHP_EOL . "Method input receive: " . PHP_EOL . print_r(MbqMain::$input, true), $ex->getFile(), $ex->getLine());
    }
}