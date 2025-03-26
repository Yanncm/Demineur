import random
import numpy as np

class Demineur:
    def __init__(self, taille=10, nb_mines=10):
        self.taille = taille
        self.nb_mines = 10
        self.grille = np.zeros((taille, taille), dtype=int)
        self.grille_visible = np.zeros((taille, taille), dtype=bool)
        self.grille_bombe = np.zeros((taille, taille), dtype=bool)
        self.generer_mines()
        self.calculer_proximite()
        

    def generer_mines(self):
        """Placement aléatoire des mines"""
        nb_mines = 0
        while nb_mines < self.nb_mines :
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
            
            if self.grille_bombe[x,y] != True :
                self.grille_bombe[x,y] = True
            nb_mines+=1

    def calculer_proximite(self):
        """Calcule le nombre de mines adjacentes pour chaque case"""
        for x in range(self.taille) :
            for y in range(self.taille) :     
                self.grille[x,y] = self.compter_mines_adjacentes(x,y)
                    
    def compter_mines_adjacentes(self, x, y):
        """Compte le nombre de mines autour d'une case"""
        mines_adja = self.mines_adjacentes(x,y,bombes=True)
        return mines_adja[0] - len(mines_adja[1])
    
    def mines_adjacentes(self,x,y,bombes=False) :
        grille = self.grille_bombe if bombes else self.grille
        resultat = []
    
        #COIN HAUT GAUCHE
        if x == 0 and y == 0 :
            if grille[x+1,y] :
                resultat.append((x+1,y))
            if grille[x+1,y+1] :
                resultat.append((x+1,y+1))
            if grille[x,y+1] :
                resultat.append((x,y+1))
            return [3,resultat]
        
        #COIN BAS GAUCHE
        if x == self.taille-1 and y == 0 :
            if grille[x,y+1] :
                resultat.append((x,y+1))
            if grille[x-1,y+1] :
                resultat.append((x-1,y+1))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            return [3,resultat]
        
        #COIN HAUT DROITE
        if x == 0 and y == self.taille-1 :
            if grille[x+1,y-1] :
                resultat.append((x+1,y-1))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            if grille[x+1,y] :
                resultat.append((x+1,y))
            return [3,resultat]
      
        #COIN BAS DROITE  
        if x == self.taille-1 and y == self.taille-1 :
            if grille[x-1,y-1] :
                resultat.append((x-1,y-1))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            return [3,resultat]
    
        #BORD HAUT
        if x == 0:
            if grille[x+1,y] :
                resultat.append((x+1,y))
            if grille[x+1,y+1] :
                resultat.append((x+1,y+1))
            if grille[x,y+1] :
                resultat.append((x,y+1))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            if grille[x+1,y-1] :
                resultat.append((x+1,y-1))
            return [5,resultat]
        
        #BORD GAUCHE
        if y == 0:
            if grille[x+1,y] :
                resultat.append((x+1,y))
            if grille[x+1,y+1] :
                resultat.append((x+1,y+1))
            if grille[x,y+1] :
                resultat.append((x,y+1))
            if grille[x-1,y+1] :
                resultat.append((x-1,y+1))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            return [5,resultat]
        
        #BORD BAS
        if x == self.taille-1:
            if grille[x,y+1] :
                resultat.append((x,y+1))
            if grille[x-1,y+1] :
                resultat.append((x-1,y+1))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            if grille[x-1,y-1] :
                resultat.append((x-1,y-1))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            return [5,resultat]
        
        #BORD DROITE
        if y == self.taille-1 :
            if grille[x+1,y] :
                resultat.append((x+1,y))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            if grille[x-1,y-1] :
                resultat.append((x-1,y-1))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            if grille[x+1,y-1] :
                resultat.append((x+1,y-1))
            return [5,resultat]
        
        #MILIEU
        else :
            if grille[x+1,y] :
                resultat.append((x+1,y))
            if grille[x+1,y+1] :
                resultat.append((x+1,y+1))
            if grille[x,y+1] :
                resultat.append((x,y+1))
            if grille[x-1,y+1] :
                resultat.append((x-1,y+1))
            if grille[x-1,y] :
                resultat.append((x-1,y))
            if grille[x-1,y-1] :
                resultat.append((x-1,y-1))
            if grille[x,y-1] :
                resultat.append((x,y-1))
            if grille[x+1,y-1] :
                resultat.append((x+1,y-1))
            return [8,resultat]

    def reveler_case(self, x, y):
        """Révèle une case et ses adjacentes si vide"""
        print("_________")
        print(x,y)
        print(type(x))
        print(type(y))
        print("_________")
        
        self.grille_visible[x,y] = True
        voisin = self.mines_adjacentes(x,y)
        for coo in voisin[1] :
            new_x,new_y = coo
            
            if self.grille[new_x,new_y] == 0 :
                self.reveler_case(new_x,new_y)
            

    def verifier_victoire(self):
        """Vérifie si toutes les cases non-mines sont révélées"""
        for x in range(self.taille) :
            for y in range(self.taille) :
                if self.grille_bombe[x,y] and self.grille_visible[x,y] :
                    return False
                if not self.grille_bombe[x,y] and not self.grille_visible[x,y] :
                    return False
        return True

    def afficher_grille(self):
        """Affiche la grille de jeu"""
        print("   " + " ".join(str(i) for i in range(self.taille)))
        for x in range(self.taille):
            ligne = f"{x}: "
            for y in range(self.taille):
                if not self.grille_visible[x, y]:
                    ligne += "■ "
                elif self.grille_bombe[x, y]:
                    ligne += "💥 "
                elif self.grille[x, y] > 0:
                    ligne += f"{self.grille[x, y]} "
                else:
                    ligne += "  "
            print(ligne)

def jouer_demineur():
    """Fonction principale du jeu"""
    jeu = Demineur(taille=5, nb_mines=5)
    
    while True:
        jeu.afficher_grille()
        jx = int(input("choissisez la ligne entre (0,9)"))
        jy = int(input("choissisez la colone entre (0,9)"))

        
        if jx == 20 or jy == 20 :
            print(jeu.grille_bombe)

        else :
            jeu.reveler_case(jx,jy)

if __name__ == "__main__":
    jouer_demineur()
