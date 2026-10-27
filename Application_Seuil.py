# Import de la bibliothèque OpenCV
import cv2
import numpy
# Chargement de l'image en niveaux de gris lena.jpg en mémoire
img = cv2.imread('Image_beton.bmp', cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy
# Affichage de l'image dans une fenêtre dont le titre est 'La belle Lena'
cv2.imshow("Du béton", img)
#Application du Seuil
retval, resultat = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
#Affichage de l'image avec Seuil
cv2.imshow("Du béton avec seuil", resultat)
cv2.waitKey(0)
#Destruction de toutes les fenêtres
cv2.destroyAllWindows()

