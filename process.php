<?php
$a = escapeshellarg($_POST['a']);
$b = escapeshellarg($_POST['b']);
$c = escapeshellarg($_POST['c']);

$command = escapeshellcmd("python3 calculate.py $a $b $c");

$output = shell_exec($command);

echo "<h2>Assignment #4</h2>";
echo "<h3>Python Script Result</h3>";

echo "<h3>Original Values:</h3>";
echo "<ul>";
echo "<li>a: $a</li>";
echo "<li>b: $b</li>";
echo "<li>c: $c</li>";
echo "</ul>";


echo "$output";
?>