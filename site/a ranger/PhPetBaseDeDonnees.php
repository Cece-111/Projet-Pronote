Syntaxe PhP pour communiquer avec une base de données

Exemple de requête INSERT avec la connexion à la base de données

<?php 
	// on se connecte à MySQL et on sélectionne la base de données
	// Il faut peut-être adapter le nom de la base de données
	$link = mysqli_connect('localhost','root','', 'NSINote');
	if ($link){
		//echo '<p>Connection réussie </p>';
		$query = "INSERT INTO matiere(nom) VALUES ('EMC')";
		//echo $query;
		// on envoie la requête
		if (mysqli_query($link,$query)) {
			echo "<p>La matière a été ajoutée.</p>";
		}
		else {
			echo "<p>La matière n'a pas pu être inserée.</p>";
		}
	
		// on ferme la connexion
		mysqli_close($link);
	}
	else {
		echo '<p>Connexion non réussie</p>';
	}
?>

Exemple de requête SELECT et affichage des résultats dans un tableau :

<?php
	$link = mysqli_connect('localhost','root','', 'NSINote');
	if ($link) {
		//echo '<p>Connection réussie </p>';

		$query = "SELECT idMatiere, nom FROM matiere";
		// on envoie la requête
		$res = mysqli_query($link,$query);

		echo "<table><tr><th>idMatiere</th><th>nom</th></tr>";
  
		// on va itérer sur chaque ligne
		while ($row = mysqli_fetch_array($res)) {
			// on affiche les résultats
			echo "<tr><td>{$row['idMatiere']}</td><td>{$row['nom']}</td></tr>";
			}
		echo "</table>";
		// on ferme la connexion
		mysqli_close($link);
		}
	else {
        echo '<p>Connexion non réussie!</p>';
         }
?>