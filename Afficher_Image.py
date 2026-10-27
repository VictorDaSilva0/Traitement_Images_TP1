# Import de la bibliothèque OpenCV
import cv2
# Chargement de l'image en niveaux de gris lena.jpg en mémoire
img = cv2.imread('Image_beton.bmp', cv2.IMREAD_GRAYSCALE) # img est un tableau Numpy
# Affichage de l'image dans une fenêtre dont le titre est 'La belle Lena'
cv2.imshow("Du béton", img)
# Mise en pause du programme jusqu'à ce que l'utilisateur appuie sur une touche
cv2.waitKey(0)
# Fermeture de toutes les fenêtres ouvertes
cv2.destroyAllWindows()
