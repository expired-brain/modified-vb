<html>
<title>IRC Controll panel</title>
<body>
<form action="" method="POST">
  <input name="shell" type="text" placeholder="CMD line..." /><br>
 <table><tbody>
  <tr>
 <td>
  <input type="checkbox" name="crime" value="1"> Run Crimeirc<br>
  <input type="checkbox" name="bad" value="1"> Run Badirc <br>
  </td>
  <td>
  <input type="checkbox" name="crime" value="0"> Stop Crimeirc<br>
  <input type="checkbox" name="bad" value="0"> Stop Badirc <br>
  </td>
  <td>
  <input type="checkbox" name="crime" value="2"> View Crimelog<br>
  <input type="checkbox" name="bad" value="2"> View Badlog <br>
  </td>

</tr>
  <tr>
  <td>
  <input type="checkbox" name="black" value="1"> Run Blackirc <br>
  <input type="checkbox" name="check" value="1"> Run Checknet <br>
</td>
<td>
  <input type="checkbox" name="black" value="0"> Stop Blackirc <br>
  <input type="checkbox" name="check" value="0"> Stop Checknet <br>
</td>
<td>
  <input type="checkbox" name="black" value="2"> View Blacklog<br>
  <input type="checkbox" name="check" value="2"> View Checklog<br>
  </td>
</tr>
</table></tbody>
    <input type="submit" name="submit" value="Submit"> <br>
    <button type="submit" name="ircprocess">Show Running IRC</button>&nbsp;&nbsp;<button type="submit" name="killall">Kill all IRC</button>
</form>
</body>
</html>


<?php

function time_elapsed_string($datetime, $full = false) {
    $now = new DateTime;
    $ago = new DateTime($datetime);
    $diff = $now->diff($ago);

    $diff->w = floor($diff->d / 7);
    $diff->d -= $diff->w * 7;

    $string = array(
        'y' => 'year',
        'm' => 'month',
        'w' => 'week',
        'd' => 'day',
        'h' => 'hour',
        'i' => 'minute',
        's' => 'second',
    );
    foreach ($string as $k => &$v) {
        if ($diff->$k) {
            $v = $diff->$k . ' ' . $v . ($diff->$k > 1 ? 's' : '');
        } else {
            unset($string[$k]);
        }
    }

    if (!$full) $string = array_slice($string, 0, 1);
    return $string ? implode(', ', $string) . ' ago' : 'just now';
}

if (isset($_POST['shell'])) {
  $p = $_POST['shell'];
  //$output = shell_exec($p);
  //explode("\n",$output);
   echo '<pre>';
   passthru($p);
   echo '</pre>';
  //echo "<pre>$output</pre>";

  // while (@ ob_end_flush()); // end all output buffers if any

  // $proc = popen($p, 'r');
  // echo '<pre>';
  // while (!feof($proc))
  // {
  //     echo fread($proc, 4096);
  //     @ flush();
  // }
  // echo '</pre>';

}

if (isset($_POST['ircprocess'])) {
  $p = 'pgrep -af python';
  echo '<pre>';
  passthru($p);
  echo '</pre>';
}

if (isset($_POST['killall'])) {
  shell_exec('pkill -f "python"');
  echo "<br> All IRC Process Should Stop Now...<br> Current running process : <br>";
  $p = 'pgrep -af python';
  echo '<pre>';
  passthru($p);
  echo '</pre>';
}
  
if (isset($_POST['crime'])) {
  $p = $_POST['crime'];
    if ($p == "1"){
      shell_exec('python run-crime.py');
      sleep(5);
      echo "CrimeIRC Started!";
      echo "Current running process : <br>";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "0")  {
      shell_exec('pkill -f "run-crime.py"');
      echo "<br> Crimeirc Should Stop Now...<br>";
      echo "Current running process : <br>";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "2")  {
      echo "Last 50 Lines from Crime log :: <br>";
      $data = array_slice(file('crime.txt'), -50);
      foreach ($data as $line) {
      echo '<pre>'.$line.'</pre>';
      }
    }
    else {
      echo "<br> Erro in input value!";
    }
}
else {
  echo  "<br>CrimeIrc :";
  echo ": Last modified: (".date("d/m H:i:s",filemtime("crime.txt")).") :: ";
  $date = date("Y-m-d H:i:s",filemtime("crime.txt"));
  echo "(".time_elapsed_string($date, true). ")";
}


if (isset($_POST['bad'])) {
  $p = $_POST['bad'];
    if ($p == "1"){
      shell_exec('python run-bad.py');
      sleep(5);
      echo "BadIRC Started!";
      echo "Current running process : <br>";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "0")  {
      shell_exec('pkill -f "run-bad.py"');
      echo "<br> BadIRC Should Stop Now...<br>";
      echo "Current running process : ";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "2")  {
      //$read = ReadFromEndByLine('bad.txt',50);
      //echo "<br>".ReadFromEndByLine('bad.txt',6);
      // $all_lines = file('bad.txt');
      // $last_5 = array_slice($all_lines , -5);
      // echo "<br>".$last_5;
      echo "Last 50 Lines from bad log :: <br>";
      $data = array_slice(file('bad.txt'), -50);
      foreach ($data as $line) {
      echo '<pre>'.$line.'</pre>';
      }
    }
    else {
      echo "<br> Erro in input value!";
    }
}
else {
  echo  "<br>BadIrc :";
  echo ": Last modified: (".date("d/m H:i:s",filemtime("bad.txt")).") :: ";
  $date = date("Y-m-d H:i:s",filemtime("bad.txt"));
  echo "(".time_elapsed_string($date, true). ")";
}


if (isset($_POST['black'])) {
  $p = $_POST['black'];
    if ($p == "1"){
      print shell_exec('python run-black.py');
      echo "BlackIRC Started!";
      echo "Current running process :";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "0")  {
      shell_exec('pkill -f "run-black.py"');
      echo "<br> BlacIRC Should Stop Now...<br>";
      echo "Current running process :";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "2")  {
      echo "Last 50 Lines from Black log :: <br>";
      $data = array_slice(file('black.txt'), -50);
      foreach ($data as $line) {
      echo '<pre>'.$line.'</pre>';
      }
    }
    else {
      echo "<br> Erro in input value!";
    }
}
else {
  echo  "<br>BlackIrc :";
  echo ": Last modified: (".date("d/m H:i:s",filemtime("black.txt")).") :: ";
  $date = date("Y-m-d H:i:s",filemtime("black.txt"));
  echo "(".time_elapsed_string($date, true). ")";
}


if (isset($_POST['check'])) {
  $p = $_POST['check'];
    if ($p == "1"){
      $q = shell_exec('python run-check.py');
      sleep(5);
      echo $q;
      echo "CheckNet Started!";
      echo "Current running process : <br>";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "0")  {
      shell_exec('pkill -f "run-check.py"');
      echo "<br> CheckNet Should Stop Now...<br>";
      echo "Current running process :";
      $p = 'pgrep -af python';
      echo '<pre>';
      passthru($p);
      echo '</pre>';
    }
    elseif ($p == "2")  {
      echo "Last 50 Lines from check log :: <br>";
      $data = array_slice(file('check.txt'), -50);
      foreach ($data as $line) {
      echo '<pre>'.$line.'</pre>';
      }
    }
    else {
      echo "<br> Erro in input value!";
    }
}
else {
  echo  "<br>CheckNet :";
  echo ": Last modified: (".date("d/m H:i:s",filemtime("check.txt")).") :: ";
  $date = date("Y-m-d H:i:s",filemtime("check.txt"));
  echo "(".time_elapsed_string($date, true). ")";
}

echo "<br>"."<br>"."<br>"."Current Server Time : " . date("Y-m-d");



// if(isset($_POST['title']) && isset($_POST['date']) && isset($_POST['list'])) {
//     $data = $_POST['date'] . '] <span style="color:#00ef5a">' . $_POST['title'];
//     $notice = $_POST['list'];
//     $ret = file_put_contents('title.txt', $data);
//     $rett = file_put_contents('list.txt', $notice);
//     if($ret == false) {
//         die('There was an error writing this file');
//         $output = shell_exec('python notice.py');
//         echo $output;
//     }
//     else {
//         echo "$ret bytes written to file";
//         $output = shell_exec('python notice.py');
//         echo "<textarea name='list' style='width:250px;height:150px;''>$output</textarea><br>";
//     }
// }
// else {
//    die('no post data to process');
// }


// $output = shell_exec('python notice.py');
// echo "<pre>$output</pre>";
?>
