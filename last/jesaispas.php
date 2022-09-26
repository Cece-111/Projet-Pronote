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
	
	if (is_numeric($Val) && is_numeric($To)) {
		
		echo "<h3>Simulation effectuée le $date à $heure :</h3><hr/>";

		if($Dev == "dollar")
		{
			$somme = round($Val,2);
			$somme = $somme*$To;
			$somme = round($somme,2);
			echo "<p>Somme obtenue : $somme dollars.</p><hr/>";
		}
		else
		{
			$somme = round($Val,2);
			$somme = $somme/$To;
			$somme = round($somme,2);
			echo "<p>Somme obtenue : $somme euros.</p><hr/>";
			}
	}
	else {
		echo "Erreur: les champs Valeur et Taux doivent contenir des valeurs numériques !";
	}
?>

	<p><a href='index.html'>Recommencer une nouvelle simulation</a></p>
</body>
</html>