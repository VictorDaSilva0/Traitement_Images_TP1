# Import de la bibliothèque OpenCV
import cv2
# Chargement de l'image de béton en niveaux de gris en mémoire
img = cv2.imread('Image_beton.bmp', cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy
# Affichage de la hauteur et de la largeur de l'image
hauteur, largeur = img.shape
print("Hauteur :", hauteur, "px - Largeur :", largeur, "px")
# Affichage de l'image originale
cv2.imshow("Du béton", img)
#Application du Seuil inverse avec Otsu : les granulats (sombres) passent en blanc, le fond en noir
retval, resultat = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#Affichage du seuil calculé par Otsu
print("Seuil de binarisation (Otsu) :", retval)
#Affichage de l'image avec Seuil inverse
cv2.imshow("Du béton avec seuil inverse", resultat)
cv2.waitKey(0)
#Destruction de toutes les fenêtres
cv2.destroyAllWindows()
