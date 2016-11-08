<?php

/**
 * Script that posts info sent to it by the Sportsticker parser as a thread in a forum
 * Based on code found in http://www.vbulletin.org/forum/showthread.php?t=97283&page=2
 *
 * @author Chris Hartjes
 */

require './global.php';
require './includes/class_dm.php';
require './includes/class_dm_threadpost.php';
require './includes/functions_databuild.php';

$threaddm = new vB_DataManager_Thread_FirstPost($vbulletin, ERRTYPE_STANDARD);
$a=array(2,4,5,6,7,8,9);
$b = $a[array_rand($a, 1)];
$post_userid = $b; 
$userid = $b;
$allow_smilie = '1';
$visible = '1';

//$vbulletin->options
$names = $vbulletin->db->query_read("SELECT username FROM user WHERE userid = $b");
$user = $db->fetch_array($names);

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


