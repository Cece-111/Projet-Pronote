<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>NSINotes</title>
        <link rel="stylesheet" type="text/css" href="style.css"> 
        <link rel="icon" type="image/x-icon" href="images/NSINotes.icon">
		<?php session_start(); ?>
    </head>
    <body> 
        <div id="barre_fixe">
            <td class="monAnnee"> <a><img id="image" src="Images/NSINotes.png" idth="200" height="50" alt="Image à venir" style="float:left;" > </a></td><h1 id="titre">NSINotes</h1>
        </div>
        <br><br><br>
        <span id="bienvenue"><h2 class="clignote"> Authentification ! </h2></span>
        <br><br>
		<?php
            if(isset($_POST['login']))
            {
				$link = mysqli_connect('localhost','root','', 'NSINote');
				if ($link){
					$query = "SELECT id, statut FROM utilisateurs WHERE nomSession = \"{$_POST['ident']}\" AND mdp = \"{$_POST['pass']}\"";
					// on envoie la requête
					$res = mysqli_query($link,$query);
					if ($res) {
						$row = mysqli_fetch_array($res);
						$_SESSION["id"] = $row['id'];
						$_SESSION["statut"] = $row['statut'];
						echo "<p> Wsh mon reuf, qui possède l'id {$_SESSION["id"]} et qui est {$_SESSION["statut"]} ! </p>";
					}
					else {
						echo "<h3 class=\"erreur\" style=\"text-align: center;\">Identifiant ou mot de passe incorrect.</h3>";
					}
					
					mysqli_close($link);
				}
				else {
					echo '<p>Connexion non réussie</p>';
				}

            }
        ?>
		<br>
        <form action="index.php" method="post">
            <table class="centrer">
                <tr>
                    <th>
                        <div class="connexion">
                            <input name="ident" type="text" class="form-control" placeholder="Identifiant" autofocus required />
                        </div>
                        <div class="connexion">
                            <input name="pass" type="password" class="form-control" placeholder="Mot de passe" style="margin: 10px 0px 0px 0px;" required />
                        </div>
                        <div class="connexion">
                            <input name="login" type="submit" class="button" value="Connexion" style="margin: 10px 0px 0px 0px;" />
                        </div>
                    </th> 
                </tr>
            </table>
        </form>
        </div>
                
    </body>
</html>