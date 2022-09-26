<!DOCTYPE html>
<html lang="fr">	

<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>Conversion euro-dollar</title>
</head>

<body>

<?php
	$Val = $_GET['valeur'];
	$To = $_GET['taux'];
	$Dev = $_GET['devise'];
	
	date_default_timezone_set('Europe/Paris');
	$date = date("d/m/Y");
	$heure = date("G\hi");
	
	echo "<h3>Il est $heure et nous somme le $date</h3><hr/>";
	
	if($Dev == 'euro')

	{
		$somme = round($Val*$To,2);
		echo "<p>Somme obtenue : $somme dollars.</p><hr/>";
	}
	else
	{
		$somme = round($Val/$To,2);
		echo "<p>Somme obtenue : $somme euro</p><hr/>";
	}
?>

	<p><a href='index.html'>Recommencer une nouvelle simulation</a></p>
</body>
</html>