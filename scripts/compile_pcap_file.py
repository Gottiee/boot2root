import os
import re

# Répertoire contenant vos fichiers source
repertoire_source = "../ft_fun"

# Liste de tous les fichiers source dans le répertoire
fichiers_source = [f for f in os.listdir(repertoire_source) if f.endswith(".pcap")]

def extract_file_number(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(lines)
            for line in reversed(lines):
                if "//file" in line:
                    print("line found")
                    number_part = line.split("//file")[1]
                    if number_part.isdigit():
                        print("number_part= ", number_part)
                        return int(number_part)
    except FileNotFoundError:
        print("error")
        pass  # Gérer le cas où le fichier n'existe pas
    except PermissionError:
        print(f"Erreur de permission pour ouvrir {filename}")
    return float('inf')  # Retourne une valeur infinie si aucune valeur n'est trouvée dans le fichier

# Triez les fichiers en fonction du numéro de fichier à la fin
fichiers_source.sort(key=extract_file_number)

# Code source résultant
code_source_final = ""

# Concaténer le contenu de tous les fichiers source dans l'ordre trié
for fichier in fichiers_source:
    chemin_fichier = os.path.join(repertoire_source, fichier)
    with open(chemin_fichier, 'r') as f:
        code_source_final += f.read()

# Écrire le code source final dans le fichier de sortie
fichier_sortie = "compile.c"
with open(fichier_sortie, 'w') as f:
    f.write(code_source_final)

print("Code source concaténé avec succès dans", fichier_sortie)
