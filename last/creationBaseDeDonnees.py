from random import *

#----------------------------CREATION BASE DE DONNEES---------------------------

script = """
CREATE TABLE IF NOT EXISTS utilisateurs (
	id	INT,
	statut	VARCHAR(255),
	nomSession	VARCHAR(255),
	mdp	VARCHAR(255),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS parents (
	id	INT CHECK (id >= 20000 AND id<=29999),
	prenom	VARCHAR(255),
	nom	VARCHAR(255),
	FOREIGN KEY(id) REFERENCES utilisateurs(id),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS professeurs (
	id	INT CHECK (id>=30000 and id<=39999),
	prenom	VARCHAR(255),
	nom	VARCHAR(255),
	FOREIGN KEY(id) REFERENCES utilisateurs(id),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS administration (
	id	INT CHECK (id>=40000 AND id<=49999),
	prenom	VARCHAR(255),
	nom	VARCHAR(255),
	FOREIGN KEY(id) REFERENCES utilisateurs(id),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS classes (
	id	VARCHAR(255),
	id_profPrincipal	INT,
	PRIMARY KEY(id),
	FOREIGN KEY(id_profPrincipal) REFERENCES professeurs(id)
);

CREATE TABLE IF NOT EXISTS eleves (
	id	INT CHECK (id>=10000 and id<=19999),
	prenom	VARCHAR(255),
	nom	VARCHAR(255),
	id_classe	VARCHAR(255),
	idResponsable_1	INT,
	idResponsable_2	INT,
	FOREIGN KEY(id) REFERENCES utilisateurs(id),
	PRIMARY KEY(id),
	FOREIGN KEY(id_classe) REFERENCES classes(id)
);

CREATE TABLE IF NOT EXISTS controles (
	id	INT,
	id_classe	VARCHAR(255),
	id_prof	INT,
	description	VARCHAR(255),
	PRIMARY KEY(id),
	FOREIGN KEY(id_classe) REFERENCES classes(id),
	FOREIGN KEY(id_prof) REFERENCES professeurs(id)
);

CREATE TABLE IF NOT EXISTS notes (
	id_controle	INT,
	id_eleve	INT,
	note	INT,
	coefficient	INT,
	FOREIGN KEY(id_controle) REFERENCES controles(id),
	FOREIGN KEY(id_eleve) REFERENCES eleves(id),
	PRIMARY KEY(id_controle,id_eleve)
);

CREATE TABLE IF NOT EXISTS appreciacions (
	id_prof	INT,
	id_eleve	INT,
	appreciation	VARCHAR(255),
	FOREIGN KEY(id_prof) REFERENCES professeurs(id),
	PRIMARY KEY(id_prof,id_eleve)
);
"""

f = open("bdd.sql","w+",encoding="utf-8")
f.write(script)

#--------------------------REMPLISSAGE BASE DE DONNEES--------------------------

#Récupération prenoms et noms
prenomsCSV = open("prenoms.csv","r", encoding = "utf-8")
nomsCSV = open("patronymes.csv","r", encoding = "utf-8")

prenoms = prenomsCSV.read().splitlines()
noms = nomsCSV.read().splitlines()

gens = []

#Création des individus
for prenom in prenoms:
    for nom in noms:
        gens.append((prenom,nom))

print(f"J'ai généré {len(gens)} individus.") #3660 individus

def renvoieRandom(L:list):
    """
    Renvoie un élément de L au hasard, tout en le supprimant de L.
    """
    return L.pop(randint(0,len(L)-1)) if len(L) > 0 else L.pop()


def genereMDP(N:int):
    """
    Génère un mot de passe aléatoire.
    """
    mdp = ""
    for i in range(N):
        i = 0
        i = randint(33,125)

        # On exclu 39 et 96, c'est à dire "`" et "'"
        # Car "`" est contraignant à écrire
        # Et "'" pose problème avec le programme
        # On évite également les doublons
        while i == 96 or i == 39 or chr(i) in mdp:
            i = randint(33,125)

        mdp += chr(i)

    # On évite que le dernier caractère soit un "\" car cela pose problème
    if mdp[-1] == "\\":
        while i == 96 or i == 39 or i == 92 or chr(i) in mdp:
            i = randint(33,125)
        mdp = mdp[:-1] + chr(i)

    return mdp

idParents = []

# Ajout des Parents
for i in range(2100):
    parent = renvoieRandom(gens)
    mdp = genereMDP(16)
    f.write(f"INSERT INTO utilisateurs VALUES({20000+i}, 'parent', '{parent[0]}.{parent[1]}{i:03d}', '{mdp}');\n")
    f.write(f"INSERT INTO parents VALUES({20000+i}, '{parent[0]}', '{parent[1]}');\n")
    idParents.append(20000+i)

idProfs = []

# Ajout des Profs
for i in range(80):
    prof = renvoieRandom(gens)
    mdp = genereMDP(16)
    f.write(f"INSERT INTO utilisateurs VALUES({30000+i}, 'professeur', '{prof[0]}.{prof[1]}{i:03d}', '{mdp}');\n")
    f.write(f"INSERT INTO professeurs VALUES({30000+i}, '{prof[0]}', '{prof[1]}');\n")
    idProfs.append(30000+i)

# Ajout de l'Administration
#/!\ Il suffit de rajouter un tuple pour rajouter d'autres fonctions
nbAdmin = 0
for elem in [(2,'cpe'),(1,'principalAdjoint'),(1,'principal')]:
    for i in range(elem[0]):
        personne = renvoieRandom(gens)
        mdp = genereMDP(16)
        f.write(f"INSERT INTO utilisateurs VALUES({40000+nbAdmin}, '{elem[1]}', '{personne[0]}.{personne[1]}{nbAdmin:03d}', '{mdp}');\n")
        f.write(f"INSERT INTO administration VALUES({40000+nbAdmin}, '{personne[0]}', '{personne[1]}');\n")
        nbAdmin += 1


# Ajout des classes
i = 0
for prefixe in ['2nde','1ère','T°']:
    for suffixe in range(1,11):
        idprof = renvoieRandom(idProfs)
        f.write(f"INSERT INTO classes VALUES('{prefixe}{suffixe}', '{idprof}');\n")

        # Ajout des eleves
        for j in range(0,randint(32,35)): #entre 32 et 35 eleves par classes

            eleve = renvoieRandom(gens)
            mdp = genereMDP(16)
            idResponsable1 = renvoieRandom(idParents)
            idResponsable2 = renvoieRandom(idParents)

            f.write(f"INSERT INTO utilisateurs VALUES({10000+i}, 'eleve', '{eleve[0]}.{eleve[1]}{i:03d}', '{mdp}');\n")
            f.write(f"INSERT INTO eleves VALUES({10000+i}, '{eleve[0]}', '{eleve[1]}', '{prefixe}{suffixe}', {idResponsable1}, {idResponsable2});\n")
            i += 1

f.close()
