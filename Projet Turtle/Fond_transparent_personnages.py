import os
from PIL import Image

def rendre_fond_transparent(chemin_entree, seuil=230):
    """
    Supprime le fond blanc d'une image et génère une copie en GIF transparent.
    """
    if not os.path.exists(chemin_entree):
        print(f"Erreur : '{chemin_entree}' introuvable.")
        return None

    # Ouvrir l'image et gérer le canal Alpha
    img = Image.open(chemin_entree).convert("RGBA")
    pixels = img.getdata()

    # Remplacement des teintes proches du blanc par du transparent pur
    nouvelles_donnees = []
    for r, g, b, a in pixels:
        if r > seuil and g > seuil and b > seuil:
            nouvelles_donnees.append((255, 255, 255, 0))
        else:
            nouvelles_donnees.append((r, g, b, a))
    img.putdata(nouvelles_donnees)

    # Préparation de la palette GIF compatible Turtle
    alpha = img.split()[-1]
    img_rgb = img.convert("RGB")
    
    # Palette limitée à 255 couleurs pour isoler l'index 0
    img_p = img_rgb.quantize(colors=255)
    
    # Masque d'opacité appliqué sur l'index 0
    masque = Image.eval(alpha, lambda a: 255 if a < 128 else 0)
    img_p.paste(0, masque)

    # Nom du fichier de sortie : "transparent_<nom_d_origine>.gif"
    nom_base = os.path.splitext(os.path.basename(chemin_entree))[0]
    chemin_sortie = f"transparent_{nom_base}.gif"

    # Enregistrement avec transparence sur la couleur 0
    img_p.save(chemin_sortie, "GIF", transparency=0)
    print(f"Succès : '{chemin_sortie}' généré.")
    return chemin_sortie


# --- LISTE DES IMAGES À TRAITER ---
# On peut ajouter ici autant de personnages qu'on veut (.gif, .png ou .jpg)
personnages_a_traiter = ["Aphrodite.gif", "Arès.gif", "Arthémis.gif", "Athéna.gif", "Cerbères.gif", "Héra.gif", "Hermès.gif", "Méduse.gif", "Cyclope.gif"]
for fichier in personnages_a_traiter:
    rendre_fond_transparent(fichier)