# Import de la bibliothèque OpenCV
import cv2
# Chargement de l'image de béton en niveaux de gris en mémoire
img = cv2.imread('Image_beton.bmp', cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy
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
#Construction de l'élément structurant de la fermeture : carré de 6x6 (vides de moins de 6 pixels)
element_fermeture = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
#Traitement 3 : Fermeture pour combler les vides dans les granulats (faux négatifs)
fermeture = cv2.morphologyEx(ouverture, cv2.MORPH_CLOSE, element_fermeture)
#Affichage de l'image après fermeture
cv2.imshow("Du béton après fermeture", fermeture)
cv2.waitKey(0)
#Destruction de toutes les fenêtres
cv2.destroyAllWindows()
