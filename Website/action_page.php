<?php
$filename = "index.html";
// Output one line until end-of-file
$lines = file($filename, FILE_IGNORE_NEW_LINES);
$lines = array_diff_key($lines, [count($lines)-1 => "xy", count($lines)-2 => "xy", count($lines)-3 => "xy"]);
// $a=array("red","green");
// array_push($a,"blue","yellow")
// $array[count($array)-2]
array_push($lines,"    <tr>");
array_push($lines,"        <td>".$_POST["Type"]."</td>");
array_push($lines,"        <td><b>Awaiting Verification</b></td>");
array_push($lines,"        <td>".$_POST["Suggestion"]."</td>");
array_push($lines,"    </tr>");
array_push($lines,"</table>");
array_push($lines,"</body>");
array_push($lines,"</html>");
$myfile = fopen("index.html", "w") or die("Unable to open file!");
foreach($lines as $value){
  fwrite($myfile, $value.PHP_EOL);
}
// for($x = 0; $x < count($lines); $x++) {
//   echo $lines[$x]."\n";
// }
echo "Thank you for your Feedback, we will check out your feedback soon!"."<br>";
echo "You will soon be redirected to the DiscordBot's UpdateLog"."<br>";
echo "If you still haven't been redirected after 5 seconds, please click <a href=\"http://discordbotupdates.luckysweb.net\">here</a>."."<br>";
header( "refresh:3;url=http://discordbotupdates.luckysweb.net/");
die();
?>