<!DOCTYPE html>
<html>
<head>
<title>Welcome to my Super Pi Webserver!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to my 2-node Supercomputer!</h1>
<p>
Nothing fancy here, yet. This is mostly for testing, learning how to run a
server, and a space for my ramblings.
Further configuration is required. Also, Shue is awesome.
</p>

<p>
PHP says: <?php echo "Hello world"; ?>
</p>
<p>
PHP says: <?php
 echo shell_exec("python3 -c \"print(3)\"");
 ?>
</p>
<?php
    $fval = isset($_POST["val"])?trim($_POST["val"]):'';   
 ?>
<form method="post">
  <input type="text" name="val">
  <input type="submit" name="colormoko">
 </form>
<p>
PHP says: <?php
    echo "$fval";
 ?>
</p>

<p>I'm running nginx (pronounced en-gin-x). Online documentation and support is
available at
<a href="http://nginx.org/">nginx.org</a>.<br/>
</p>

<p>
Contents:
<blockquote>
<em>
<a href="blog-20170520.html">2017-05-20</a><br/>
<a href="blog-20170604.html">2017-06-04</a><br/>
<a href="blog-20170605.html">2017-06-05</a><br/>
<a href="blog-20170614.html">2017-06-14</a><br/>
<a href="thingsnobodycaresaboutbutme.html">yourcalendricalfallacies</a><br/>
<a href="shuesblog/">Shue's blog</a><br/>
</em>
</blockquote>
</p>

</body>


<style>
	.bottom-three {
		margin-bottom: 5cm;
	}
</style>
<p class="bottom-three">
<div id="footer">
<em>
<a href="http://freedns.afraid.org/">Free DNS</a></br>
<a href="http://1-node-supercomputer.strangled.net">1-node-supercomputer.strangled.net</a></br>
<a href="http://2-node-supercomputer.spacetechnology.net">2-node-supercomputer.spacetechnology.net</a><br/>
</em>
</div>
</p>

</html>
