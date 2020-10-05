"""

Script



"""




# Décalration des paquets

import tkinter as tk    # Pour interface graphique
import os    # Pour chemins des fichiers
from tkinter import filedialog as FD    # Pour boîte de dialogue de sélection de l'image
from PIL import Image, ImageTk      # Pour traitement, sélection, affichage de l'image comme canevas
import json     # Pour export en fichier .json

# Fin de déclaration des paquets





# Défintiion de la 1ère classe: l'interface graphique du programme
class Fenetre_principale(tk.Tk):    # Création de la classe
    def __init__(self, master):     # Création init de la classe

    # Le cadre principal
        self.cadre_principal = tk.Frame(master=master)  # Création du cadre, son emplacement et ses caractéristiques
        self.cadre_principal.pack(fill=tk.BOTH, expand=1)   # Affichage du cadre et de sa taille

    # Les éléments du cadre principal
        # Le titre
        self.label_titre = tk.Label(master=self.cadre_principal, text="Application pour labelliser les images", font=("FreeSerif", 16), background="red")   # Création du titre et de ses caractéristiques
        self.label_titre.pack(side=tk.TOP, fill=tk.X, expand=0)     # Affichage du titre

        # Le 2ème cadre
        self.deuxieme_cadre = tk.Frame(master=self.cadre_principal, background="lightgray")  # Création du cadre, son emplacement et ses caractéristiques
        self.deuxieme_cadre.pack(side=tk.TOP, fill=tk.BOTH, expand=1) # Affichage du cadre et de sa taille

        # Zone d'affichage de l'image "canevas"
        self.zone_affichage_image = tk.Canvas(master=self.deuxieme_cadre, background="white")   # Création du canevas pour l'image
        self.zone_affichage_image.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)    # Affichage du canevas pour l'image

    # Le cadre des paramètres
        self.zone_parametres = tk.Frame(master=self.deuxieme_cadre, borderwidth=20, background="lightgray")  # Création du cadre, son emplacement et ses caractéristiques
        self.zone_parametres.pack(side="right", fill=tk.BOTH, expand=1)     # Affichage du cadre et de sa taille

        # Liste des étiquettes
            # Interface des étiquettes
        self.message_etiquettes = tk.Label(master=self.zone_parametres, text="Étiquettes", background="lightgray")  # Création du titre pour les étiquettes
        self.message_etiquettes.pack(side="top", fill=tk.X, expand=1)   # Affichage du titre pour les étiquettes
        
            # Affiliation des noms des étiquettes provenant du fichier "labels.txt" aux étiquettes: récupération du texte et pour chaque 
            # pour qu'il apparaisse l'un en dessous de l'autre dans la barre de défilement.
        with open("labels.txt") as fichier_labels:  # Affiliation du fichier de labels.txt à une variable
            liste_de_lignes = fichier_labels.readlines()    # Lecture des lignes de la variable du fichier
            liste_de_labels = []    # Enregistrement des labels comme liste
            for line in liste_de_lignes:    # Boucle de lecture des labels
                liste_de_labels.append(line.strip())    # Ajoute une élément à la liste de labels
        self.chaine_characters = tk.StringVar(self.zone_parametres)  # Mémorisation de la chaîne de caractères
        self.bases = tk.OptionMenu(self.zone_parametres, self.chaine_characters, *liste_de_labels, command=self.change_labels)   # Création du menu de sélection des labels et de ses caractéristiques et de la commande affiliée au bouton
        self.bases.pack()   # Affichage du menu de sélection des labels

        # Bouton sauvegarder
        self.bouton_sauvegarder = tk.Button(master=self.zone_parametres, text="Sauvegarder")    # Création du bouton sauvegarder SANS a commande, le bouton ne fonctinne pas
        self.bouton_sauvegarder.pack(side="top", fill=tk.X, expand=1)   # Affichage du bouton sauvegarder

        # Bouton supprimer
        self.bouton_supprimer = tk.Button(master=self.zone_parametres, text="Supprimer", command=self.supprimer_fichiers)   # Création du boton supprimer un fichier et commande associée à la def
        self.bouton_supprimer.pack(side="bottom", fill=tk.X, expand=1)  # Affichage du bouton supprimer

        # Bouton Ajouter
        self.bouton_ajouter = tk.Button(master=self.zone_parametres, text="Ajouter", command=self.ajouter_fichiers)     # Création du bouton ajouter un fichier et commande associée à la def
        self.bouton_ajouter.pack(side="bottom", fill=tk.X, expand=1)    # Affichage du bouton ajouter un fichier

        # Affichage liste des images
            # Cadre de la liste
        self.liste_images = tk.Frame(master=self.zone_parametres)   # Déclaration du cadre, son emplacement et ses caractéristiques
        self.liste_images.pack(side="bottom", fill=tk.X, expand=0)  # Affichage du cadre et de sa taille

            # Scroll de la liste des images
        self.cbar = tk.Scrollbar(master=self.liste_images)  # Création de la barre de défilement "scrollbar" pour la liste d'images 
        self.cbar.pack(side=tk.RIGHT, fill=tk.Y, expand=0)  # Affichage de la barre de défilement

            # Contenu de la liste des images
        self.liste_chemin = tk.Listbox(master=self.liste_images, yscrollcommand=self.cbar.set)  # Création du contenu de la liste pour les images
        self.liste_chemin.pack(side="bottom", fill=tk.X, expand=1)  # Affichage du contenu pour la liste

            # Titre de la liste d'Images
        self.message_liste_images = tk.Label(master=self.zone_parametres, text="Liste d'images", background="lightgray")    # Création du titre pour la liste des images
        self.message_liste_images.pack(side="bottom", fill=tk.X, expand=1)  # Affichage du titre pour laliste des images

        # Bouton Ouvrir
        self.bouton_ouvrir_image = tk.Button(master=self.zone_parametres, text="Ouvrir une image", command=self.ouvrir_image)   # Création du bouton ouvrir une image et commande associée à la def
        self.bouton_ouvrir_image.pack(side="bottom", fill=tk.X, expand=1)   # Affichage du bouton ouvrir l'image


    # Les fonctions utilisées dans la classe de l'interface graphique
        # Définition de la fonction utilisée pour l'affichage des labels à partir du fichier txt.
    def change_labels(self, x):     # Déclaration de la fonction
        print(self.chaine_characters.get())     # Commande pour la lste des labels: récupération des labels


        # Définition des fonctions des boutons utilisés dans la zone des paramètres
            # Définition de la fonction du bouton charger
    def ajouter_fichiers(self):     # Déclaration de la fonction
        global chemin   # Déclaration de la variable chemin en globale pour l'utiliser partout
        chemins = FD.askopenfilenames()     # Ouverture de la boite de dialogue pour sélectionner image
        if not chemins:     # Si pas de chemin, pas de sélection
            return  # Fin de la boucle
        self.chemins_des_images = list(chemins)     # Création d'une liste pour les chemins
        self.liste_chemin.delete(0, tk.END)     # Supprimer liste des chemins
        for chemin in self.chemins_des_images:  # Pour chaque chemin de la liste:
            name = os.path.basename(chemin)     # Donne le nom du fichier
            self.dirname = os.path.dirname(chemin)  # Donne le chemin du fichier
            self.liste_chemin.insert(tk.END, name)  # Insertion du nom du ficher
        return  # Fin de la boucle

            # Définition de la fonction du bouton supprimer
    def supprimer_fichiers(self):   # Déclaration de la fonction
        global chemin   # Déclaration de la variable chemin pour globale pour l'utiliser partout
        chemin = self.liste_chemin.curselection()   # Affiliation de la sélection pour la suppression à ue variable
        indice_de_selection = chemin[0]     # Retrouve chemin de la sélection
        name = self.liste_chemin.get(indice_de_selection)   # Enregistrement de la sélction à une variable
        chemins = []    # Créatin de la liste de chemins
        supprime_chemin = os.path.join(self.dirname, name)  # Affiliatin du chemin à supprimer à une variable
        print("chemin à supprimer:", supprime_chemin)   # Afficher le message pour supprimer
        print("chemins", str(self.chemins_des_images))  # Afficher le chemin
        for chem in self.chemins_des_images:    # Pour un élément dans les chemins:
            if supprime_chemin != chem:     # Si le chemin à supprimer ne correspond pas à l'élement
                chemins.append(chem)    # Ajout d'un élément chemin
        self.chemins_des_images = chemins   # Les éléments se correspondent donc nouveau chemin
        print("nouveaux chemins:", str(self.chemins_des_images))    # Afficher message
        self.liste_chemin.delete(indice_de_selection)   # Supprimer le chemin sélectionné
        return  # Fin de la fonction

            # Défintion de la fonction pour ouvrir une image
    def ouvrir_image(self):     # Déclaration de la fonction
        selection = self.liste_chemin.curselection()    # Sélection de l'image à ouvrir
        indice_de_selection = selection[0]  # Retrouve chemin sélection
        name = self.liste_chemin.get(indice_de_selection)   # Enregistrement de la sélection à une variable
        cheminabsolu = os.path.join(self.dirname, name)     # Affiliation du chemin absolu de l'image à afficher
        image = Image.open(cheminabsolu)    # Ouvrir l'image du chemin absolu sélectionné
        self.photo = ImageTk.PhotoImage(image)  # Affichage de l'image
                # Association direct du scroll  à l'ouverture de l'image
        self.zone_affichage_image.create_image(0,0, anchor = tk.NW, image=self.photo)   # Création de l'image dans la zone pour l'image
                    # Appel de la class Image Scrollable et caractéristiques d'affchage
        Image_Scrollable(master=self.zone_affichage_image, image=self.photo, width=200, height=200).pack(side=tk.LEFT, fill=tk.BOTH, expand=1) 
        self.zone_affichage_image = Image_Scrollable()  # Affiiation de la classe Image scrollable à la zone d'affichage de l'image
# Fin de la classe: interface graphique


# Définition de la classe pour scroller les images et pour faire les rectangles de sélection
class Image_Scrollable(tk.Canvas):  # Déclaration de la classe
    def __init__(self, master=None, **kw):  # Déclaration init de la classe
        self.photo = kw.pop('image', None)  # Affiliation à l'image ouverte précédemment
        super(Image_Scrollable, self).__init__(master=master, **kw) # Gestion "super" des classes pour affiliation à l'autre classe
        self['highlightthickness'] = 1  # Épaisseur de la ligne
        self.propagate(0) # Ne rien faire si rien n'est fait
        self.create_image(0,0, anchor='nw', image=self.photo)   # Création  de l'image

    # Scrollbars verticaux et horizontaux
        self.scroll_vertical = tk.Scrollbar(self, orient='vertical', width=6)   # Création du scrollbar vertical
        self.scroll_horizontal = tk.Scrollbar(self, orient='horizontal', width=6)   # Création du scrollbar horizontal
        self.scroll_vertical.pack(side='right', fill='y')   # Affichage du scrollbar vertical
        self.scroll_horizontal.pack(side='bottom', fill='x')    # Affichage du scrollbar horizontal

    # Fixer les scrollbars sur le canevas
        self.config(xscrollcommand=self.scroll_horizontal.set, yscrollcommand=self.scroll_vertical.set)     # Configuration de la zone des scrollbars
        self.scroll_vertical.config(command=self.yview)     # Configuration du scrollbar vertical
        self.scroll_horizontal.config(command=self.xview)   # Configuration du scrollbar horizontal
        
    # L'endroit qui doit être scrollé
        self.config(scrollregion=self.bbox('all'))  # Création de la zone du scrollbar
        self.focus_set()    # Désigne l'endroit sur lequel focus
        
    # La fonction "scroll"
        self.bind_class(self, self.scroll_de_l_image)   # Appel de la fonction scroll définie

    # Les fonctions appuyer et relacher souris pour former le rectangle de sélection: apellées ici pour les associer directement à l'image
        self.x = self.y = 0     # Coordonnées avant la création des rectangles de sélection
        self.bind("<ButtonPress-1>", self.appuyer_souris)   # Appel de la fonction appuyer souris définie
        self.bind("<ButtonRelease-1>", self.relacher_souris)    # Appel de la fonction relacher souris définie

    # Définition des fonctions pour la classe Image scrollable
        # Fonction utilisée pour scroller l'image:
    def scroll_de_l_image(self, event):     # Déclaration de la fonction
        if action.state == 0 :  # Si déplacement vers le bas
            self.yview_scroll(-1*(action.delta), 'units')   # Bouger vers le bas
        if action.state == 1:   # Si déplacement vers le haut
            self.xview_scroll(-1*(action.delta), 'units')   # Bouger vers le haut

        # Fonction pour appuyer sur la souris pour former le rectangle
    def appuyer_souris(self, event):    # Déclaration de la fonction
        self.x = event.x    # Premier clik souris = coordonnées X
        self.y = event.y    # Premier click souris = coordonnées Y

        # Fonction pour appuer sur la souris pour arreter le rectangle
    def relacher_souris(self, event):   # Déclaration de la fonction
        x0,y0 = (self.x, self.y)    # Affiliation de variables aux coordonnées du premier click
        x1,y1 = (event.x, event.y)  # Affiliation de variables aux coordonnées du deuxième click
        self.create_rectangle(x0,y0,x1,y1, fill="red")  # Création de rectangles rouge pour la sélection
        self.coords(x0,y0,x1,y1)    # Association des coordonnées aux variables

# Fin de la classe: scroll des images




"""
Essai d'enregistrement des coordonnées dans un fichier .json

    # Définition de la fonction : enregistrement des coordonnées en fichier .json
    def coordonnees_to_json(self, event):
        label=self.liste_labels.curselection()
        variables_coordonnees=x0,y0,x1,y1.get()
        coordonnees = [
            for d in variables_coordonnees:
            x = {
            "chemin_image: " chemin
            "label:" label
            "topleft": haut_gauche
            "bottomright": bas_droite
        },
        {
            "label": label2
            "topleft": haut_gauche2
            "bottomright": bas_droite2
        },
        {
            "label": label3
            "topleft": haut_gauche3
            "bottomright": bas_droite3
        }]
        return json.dumps(sortie, indent=10)

        fichier_json = open("Coordonnees_image.json", "a")
        fichier_json.write(variables_coordonnees)

"""




if __name__ == "__main__":
    root = tk.Tk()
    monapp = Fenetre_principale(root)
    root.mainloop()
