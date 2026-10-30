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

# Q6 : La fonction de détection des contours utilisée ultérieurement suppose que les objets sont blancs sur fond noir. En tenant compte de l’apparence des granulats sur l’image originale, expliquer pourquoi une binarisation inverse est nécessaire.

Les granulats sont plus sombres que le béton. Avec une binarisation classique, les pixels au-dessus du seuil (le béton) passent à 255 : le béton devient blanc et les granulats noirs, donc findContours détecterait le béton comme un seul gros objet. Avec la binarisation inverse (THRESH_BINARY_INV), ce sont les pixels sous le seuil qui passent à 255 : les granulats deviennent blancs sur fond noir. C'est aussi nécessaire pour l'ouverture et la fermeture, qui agissent sur les objets blancs.

# Q7 : Sur l’image binarisée obtenue, les granulats semblent-ils tous correctement détectés ? Si non, quels défauts observe-t-on ?

Non. Les gros granulats sont bien détectés mais l'image binarisée contient 247 objets blancs alors qu'on voit une dizaine de granulats. On observe :
- beaucoup de petits points blancs isolés (faux positifs) : impuretés, pores, grain du béton ;
- une fine ligne blanche en haut de l'image, car la première ligne de pixels est plus sombre (défaut d'acquisition) ;
- des trous noirs et des bords déchiquetés dans les granulats (faux négatifs), surtout sur le bord gauche du gros granulat en haut à droite qui est découpé en plusieurs morceaux.

# Q8 : Pourquoi l’ouverture supprime-t-elle les impuretés ? Votre réponse doit faire apparaître les mots « érosion » et « dilatation ».

L'ouverture est une érosion suivie d'une dilatation avec le même élément structurant (carré 6x6). L'érosion ne garde un pixel blanc que si l'élément structurant tient entièrement dans l'objet : les impuretés plus petites que 6x6 disparaissent complètement, les granulats sont seulement amincis. La dilatation redonne ensuite aux granulats leur taille d'origine, mais elle ne peut pas faire réapparaître les impuretés puisqu'il ne reste plus aucun de leurs pixels. On passe de 247 objets à 19 objets.

# Q9 : Que se passerait-il si le traitement 3 était réalisé avant le traitement 2 ?

La fermeture agirait aussi sur les impuretés : les petits points proches les uns des autres seraient soudés en taches plus grandes que le carré 6x6, que l'ouverture ne pourrait plus supprimer. Les impuretés collées au bord des granulats y seraient aussi rattachées. En testant, on obtient 20 objets au lieu de 15 et les granulats sont plus gros (24543.5 px -> 25555.5 px pour le plus gros).

# Q10 : Le nombre de granulats détectés correspond-il visuellement à ce qu’on observe sur l’image ? Si ce n’est pas le cas, proposer une explication.

Non, on détecte 15 granulats alors qu'on en voit 6 gros (n°4, 5, 7, 9, 12, 15) et environ 4 petits (n°8, 10, 11, 13). Les autres sont des artefacts :
- n°1 et 14 (9.5 et 21 px) : des fragments dans les coins de l'image. Ils survivent à l'ouverture car OpenCV n'érode pas les objets depuis l'extérieur de l'image ;
- n°2 : le coin en bas à gauche de l'image qui est plus sombre ;
- n°3 : une tache ronde plus claire que les granulats, sûrement un pore ou une bulle d'air ;
- n°6 : une petite impureté un peu plus grande que le carré 6x6.

On pourrait les éliminer avec une aire minimale. De plus, les granulats 4 et 15 touchent le bord de l'image donc ils sont coupés.

# Q11 : Quelle est l’aire moyenne des granulats. En quelle unité est exprimée cette aire ?

L'aire moyenne est de 3816.97 px. Elle est exprimée en pixels (pixels carrés), pas en unité physique : pour l'avoir en mm² il faudrait connaître la taille réelle d'un pixel (étalonnage avec une règle par exemple).

# Q12 : L’aire moyenne semble-t-elle être un indicateur pertinent pour décrire cette population de granulats ?

Non. Les aires sont très dispersées (de 9.5 px à 24543.5 px, écart-type de 6878 px, plus grand que la moyenne). Seuls 4 granulats sur 15 dépassent la moyenne et les 6 plus gros représentent 98 % de la surface totale. La médiane (163 px) est 23 fois plus petite que la moyenne, qui ne représente donc aucun granulat réel. Elle est en plus faussée par les fausses détections. Il vaudrait mieux donner la répartition des tailles (histogramme), la médiane, ou le pourcentage de surface occupé par le caoutchouc (13 % de l'image).
