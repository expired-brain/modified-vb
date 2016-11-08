<?php

/**
 * Script that posts info sent to it by the Sportsticker parser as a thread in a forum
 * Based on code found in http://www.vbulletin.org/forum/showthread.php?t=97283&page=2
 *
 * @author Chris Hartjes
 */

require '../global.php';
require '../includes/class_dm.php';
require '../includes/class_dm_threadpost.php';
require '../includes/functions_databuild.php';

$a=array(1,2,3,4,5,6);
//$b=array_rand($a,1);
$b = 2;
//$b will be the id of user id post userid 
$threaddm = new vB_DataManager_Thread_FirstPost($vbulletin, ERRTYPE_STANDARD);
$post_userid = $b; // Admin
$userid = $b;
//$user_name = 'Expired';
$allow_smilie = '1';
$visible = '1';

//;selcet f
//
//$shout = $vbulletin->db->query_read( "SELECT id, idaut, name, message, time FROM mkp_urlobox ORDER BY 'id' DESC LIMIT 10");
// $name = $shout['idaut'];
// $message = $shout['message'];

//$vbulletin->options
$names = $vbulletin->db->query_read("SELECT username FROM user WHERE userid = $b");
$user = $db->fetch_array($names);
//$vbulletin->user['username'];
//echo $user[1];
//$user = var_dump($user);
echo $b;
echo $user["username"];
//) { ["username"]=> string(7) "expired" }
/*foreach $names as $name
echo $name['username'];*/
//echo $name;

//$name = $shout['idaut'];
//echo $user_name;


if (isset($_POST['forum_id'])) $forum_id = (int)$_POST['forum_id'];
if (isset($_POST['post_text'])) $post_text = (string)strip_tags($_POST['post_text']);
if (isset($_POST['title'])) $title = (string)strip_tags($_POST['title']);

$threaddm->do_set('forumid', $forum_id);
$threaddm->do_set('postuserid', $b);
$threaddm->do_set('userid', $b);
$threaddm->do_set('username', $user["username"]);
$threaddm->do_set('pagetext', $post_text);
$threaddm->do_set('title', $title);
$threaddm->do_set('allowsmilie', $allow_smilie);
$threaddm->do_set('visible', $visible);
$threaddm->save();
build_forum_counters($forum_id);

?>


