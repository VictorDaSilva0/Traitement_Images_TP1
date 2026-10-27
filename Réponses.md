# Q1 : En consultant cette aide, indiquer quel est le rôle de la fonction OpenCV waitKey. Que se passe-t-il quand le paramètre vaut zéro ? Que représente la valeur de retour ?

La fonction waitKey attend qu'une touche soit pressée. Si la valeur est à 0 cela veut qu'elle attendra jusqu'à ce qu'une touche soit pressé car cette valeur représente le temps d'attente en milisecondes. La valeur de retour représente soit la touche pressé, soit -1 si une durée a été determinée et qu'aucune touche n'a été pressé.

# Q2 : Pourquoi le tableau qui contient l’image de béton est-il à deux dimensions ? Dans quel cas une image est-elle stockée dans un tableau à trois dimensions ?

Etant donné que l'image est en niveau de gris, les dimensions sont donc Longueur et Hauteur ce qui donne un tableau 2D. Si c'était une image en BGR, là nous aurions un tableau 3D.

# Q3 : Les granulats apparaissent-ils plus sombre ou plus clair que le fond ?

Les granulats apparaissent plus sombres.

