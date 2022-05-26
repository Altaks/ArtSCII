from PIL import Image

# ouvrir l'image
image = Image.open("image/image.png")

# changer la taille de l'image
image = image.resize((50, 50))

ASCII_art_niveaux = [".", ",", "'", ":", ";", "+", "*", "&", "#", "@"]

# préparer le tableau de pixels
tab = [[None for i in range(image.size[0])] for j in range(image.size[1])]

# récupérer tous les pixels de l'image
for x in range(image.size[0]):
    for y in range(image.size[1]):
        tab[y][x] = image.getpixel((x, y))

# convertir toutes les couleurs en niveau de gris sur 20 niveaux
for x in range(image.size[0]):
    for y in range(image.size[1]):
        tab[y][x] = ASCII_art_niveaux[
            int(
                (tab[y][x][0] + tab[y][x][1] + tab[y][x][2]) / 3
                        * (len(ASCII_art_niveaux) - 1) / 255)
        ]

# reformer chaque ligne
result = []
for ligne in tab:
    result.append("".join(ligne))

final_image = "\n".join(result)

# écrire dans un fichier
with open("image/image.txt", "w+") as f:
    f.write(final_image)