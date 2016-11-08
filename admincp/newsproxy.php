<?php
/*======================================================================*\
|| #################################################################### ||
|| # vBulletin 3.8.9 - Licence Number VBFE810A2D
|| # ---------------------------------------------------------------- # ||
|| # Copyright ©2000-2015 vBulletin Solutions, Inc. All Rights Reserved. ||
|| # This file may not be redistributed in whole or significant part. # ||
|| # ---------------- VBULLETIN IS NOT FREE SOFTWARE ---------------- # ||
|| # http://www.vbulletin.com | http://www.vbulletin.com/license.html # ||
|| #################################################################### ||
\*======================================================================*/

// ######################## SET PHP ENVIRONMENT ###########################
error_reporting(E_ALL & ~E_NOTICE);

// ##################### DEFINE IMPORTANT CONSTANTS #######################
define('CVS_REVISION', '$RCSfile$ - $Revision: 80813 $');

// #################### PRE-CACHE TEMPLATES AND DATA ######################
$phrasegroups = array();

$specialtemplates = array();

// ########################## REQUIRE BACK-END ############################
require_once('./global.php');
require_once(DIR . '/includes/class_rss_poster.php');

header('Content-Type: text/xml; charset=utf-8');

/*======================================================================*\
|| ####################################################################
|| # Downloaded: 18:59, Mon Jul 11th 2016
|| # CVS: $RCSfile$ - $Revision: 80813 $
|| ####################################################################
\*======================================================================*/
?>