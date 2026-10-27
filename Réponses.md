# Q1 : En consultant cette aide, indiquer quel est le rôle de la fonction OpenCV waitKey. Que se passe-t-il quand le paramètre vaut zéro ? Que représente la valeur de retour ?

La fonction waitKey attend qu'une touche soit pressée. Si la valeur est à 0 cela veut qu'elle attendra jusqu'à ce qu'une touche soit pressé car cette valeur représente le temps d'attente en milisecondes. La valeur de retour représente soit la touche pressé, soit -1 si une durée a été determinée et qu'aucune touche n'a été pressé.

# Q2 : Pourquoi le tableau qui contient l’image de béton est-il à deux dimensions ? Dans quel cas une image est-elle stockée dans un tableau à trois dimensions ?

Etant donné que l'image est en niveau de gris, les dimensions sont donc Longueur et Hauteur ce qui donne un tableau 2D. Si c'était une image en BGR, là nous aurions un tableau 3D.

# Q3 : Les granulats apparaissent-ils plus sombre ou plus clair que le fond ?

Les granulats apparaissent plus sombres.

# Q4 : Indiquer les termes consacrés, vus durant le cours magistral, correspondant aux trois étapes ci-dessous.

1. Détection de deux classes de pixels : le fond et les granulats de caoutchouc (autrement dit : séparation des objets et du fond). Opération de Binarisation

2. Élimination des faux positifs, c’est-à-dire des petits éléments détectés comme des granulats de caoutchouc, mais qui sont en réalité des impuretés. 
Opération d'Ouverture

3. Élimination des faux négatifs, c’est-à-dire des éléments détectés comme du fond alors qu’ils font partie des granulats (pixels noirs dans un granulat). 
Opération de Fermeture

# Q5 : Le seuil calculé automatiquement par Otsu semble-t-il cohérent avec l’image observée ?Justifier.

En partie oui, une grande partie des bouts de caoutchouc détectés correspondent bien à ceux présent dans le bloc de béton.
