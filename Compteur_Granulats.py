# Import de la bibliothèque OpenCV
import cv2
# Chargement de l'image de béton en niveaux de gris en mémoire
img = cv2.imread('Image_beton.bmp', cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy
# Affichage de la hauteur et de la largeur de l'image
hauteur, largeur = img.shape
print("Hauteur :", hauteur, "px - Largeur :", largeur, "px")
# Affichage de l'image originale
cv2.imshow("Du béton", img)

#Traitement 1 : Binarisation inverse avec Otsu (granulats en blanc, fond en noir)
retval, resultat = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print("Seuil de binarisation (Otsu) :", retval)
cv2.imshow("Du béton avec seuil inverse", resultat)

#Traitement 2 : Ouverture avec un élément structurant carré de 6x6 (suppression des impuretés)
element_ouverture = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
ouverture = cv2.morphologyEx(resultat, cv2.MORPH_OPEN, element_ouverture)
cv2.imshow("Du béton après ouverture", ouverture)

#Traitement 3 : Fermeture avec un élément structurant carré de 6x6 (comblement des vides)
element_fermeture = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
fermeture = cv2.morphologyEx(ouverture, cv2.MORPH_CLOSE, element_fermeture)
cv2.imshow("Du béton après fermeture", fermeture)

#Détection des contours externes des granulats, sans approximation (la hiérarchie n'est pas récupérée)
contours, _ = cv2.findContours(fermeture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#Affichage du nombre de granulats (nombre de cases du tableau contours)
print("Nombre de granulats :", len(contours))

#Copie de l'image originale pour y dessiner les résultats sans modifier img
img_resultat = img.copy()
#Dessin de tous les contours (-1) en blanc (255) avec une épaisseur de 2 pixels
cv2.drawContours(img_resultat, contours, -1, 255, 2)

#Affichage du numéro et de l'aire de chaque granulat + numéro écrit sur l'image
somme_aires = 0
for i in range(len(contours)):
    aire = cv2.contourArea(contours[i])
    somme_aires = somme_aires + aire
    print("Granulat", i + 1, "- Aire:", aire, "px")
    #Rectangle englobant le granulat : le numéro est écrit en son centre
    x, y, w, h = cv2.boundingRect(contours[i])
    cv2.putText(img_resultat, str(i + 1), (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 2)

#Calcul et affichage de l'aire moyenne des granulats
if len(contours) > 0:
    aire_moyenne = somme_aires / len(contours)
    print("Aire moyenne :", round(aire_moyenne, 2), "px")

#Affichage de l'image finale avec les contours et les numéros des granulats
cv2.imshow("Granulats détectés", img_resultat)
cv2.waitKey(0)
#Destruction de toutes les fenêtres
cv2.destroyAllWindows()
