from time import sleep
from random import random,randint

print("LA GRANDE AVENTURE !\n")
#Gagner un niveau
expnecessaire = 5
def niveaux():
    global vietotale
    global classe
    global expnecessaire
    niveauTemp = int(niveau[0])
    expnecessaire = expnecessaire+2*niveauTemp
    if exp[0] >= expnecessaire :
        niveau[0] = niveau[0] + 1
        exp[0] = 0
        niv = niveau[0]
        print("Vous êtes maintenant niveau", niv,"!")
        if classe == "Dieu créateur" :
            attaque == 1000000
            attaque[0] = 1000000
            vietotale = 1000000
            vie[0] = 1000000
        else :
            if classe == "Magicien" :
                attaque[0] = 2+4*niveau[0]
                vietotale = 10+3*niveau[0]
            elif classe == "Épéiste" :
                attaque[0] = 2+2*niveau[0]
                vietotale = 10+4*niveau[0]
            elif classe == "Paysan" :
                attaque[0] = 2+2*niveau[0]
                vietotale = 10+3*niveau[0]
            if vie[0]<vietotale:
                vie[0] = vietotale

#Racourci
def faire ():
    global classe
    commandes(classe)



#Affiche le contenu de l'inventaire
def inventaire(inventaire):
    print ( "Inventaire :")
    for i in range (len(inventaire)):
        print("-"+inventaire[i])
    "\n"

#Commande pour utiliser les potions de l'inventaire
def utiliser():
    global vietotale
    
    if len(inventaire) <=0:
        print("Vous n'avez pas de potions.")
    else :
        print("Slurp...Sah, elle est bonne cette potion !")
        print("Je sens que je reprend des forces...")
        del inventaire[0]
        vie[0] += 5
        if (vie[0] > vietotale) :
            vie[0] = vietotale
        print("Vie :",vie[0],"/",vietotale)

#Acheter
def magasin():
    if _or[0]<5:
        print("Désolé, mais vous n'avez pas assez d'or.\n")
    else :
        choix = input("Voulez vous acheter quelque chose ? ")
        print()
        choix.upper()
        if choix == "POTION" or choix == "1":
            _or[0]= _or[0] - 5
            inventaire.append("Potion")
            print("Vous achetez une potion.")
            sleep(0.5)
            or_ = _or[0]
            print("Il vous reste,",or_,"d'or.\n")
            sleep(0.5)
            shop()
        elif choix == "AUTRE" or choix == "2":
            print("Désolé mais nous n'avons rien d'autre pour le moment.\n")
            magasin()
        elif choix == "" or choix == "NON":
            print("Vous sortez du magasin.")

        else : 
            print("Choisissez parmis le stock s'il vous plaît.\n")
            magasin()


        



#Shop
def shop():
    print("Approchez ! Approchez messieurs dames !")
    sleep(0.25)
    print("J'ai tout ce qu'il vous faut !\n")
    sleep(0.5)
    nb = len(inventaire)
    print("Vous avez",nb,"potions dans votre inventaire.")
    sleep(0.5)
    or_ = _or[0]
    print("Vous avez",or_,"pièces d'or.\n")
    sleep(0.5)
    print("-Acheter(1)")
    sleep(0.5)
    print("-Partir(2)\n")
    sleep(0.5)
    choix = input("Votre choix : ")
    print()
    choix.upper()
    if choix == "PARTIR" or choix == "2":
        print("Vous partez du magasin.\n")
        sleep(0.5)
    elif choix == "ACHETER" or choix == "1":
        print ("Potions(1)")
        sleep(0.5)
        print ("Autre(2)\n")
        sleep(0.5)
        magasin()

#Récompenses
def recompense(nom,niveauMonstre):
    global classe
    if (nom == "Roi Démon"):
        print
        print("'Bien joué, Héros.'")
        sleep(0.5)
        print("'Tu as vaincus celui qui nous menaçait tous !'")
        sleep(0.75)
        if classe == "Paysan":
            print("'Je ne sais pas comment toi, un simple paysan a réussi, mais cela ne change rien !'")
            sleep(1)
        print("'Maintenant, la seule menace à notre monde, c'est toi !'")
        sleep(1)
        if classe == "Dieu créateur":
            print("Tandis que le mage Paysouf essait de vous éradiquer de la surface de son monde vous le regarder de tout votre statut et l'écrasez.\n")
            sleep(2)
            print("FIN\n")
            sleep(0.5)
            print("Merci d'avoir joué !")
            sleep(10)
            exit()
        else:
            print("Vous sentez une vive douleur dans votre mains droite, tandis que vous la regardez, vous la voyez fondre, ne laissant rien.")
            sleep(2)
            print("Tandis que tout votre être disparait, vos larme tombe sur le sol et vous mourrez.\n")
            sleep(2)
            print("FIN\n")
            sleep(0.5)
            print("Merci d'avoir joué !")
            sleep(10)
            exit()
    else :
        print("Vous avez vaincus un",nom,"!")
        sleep(0.5)
        prix = randint(1,4)
        print("Vous gagnez",prix,"pièces d'or !")
        sleep(0.5)
        xp = randint(1,5)
        print("vous gagnez ", xp,"exp !")
        exptotale = exp[0] + xp
        or_ = _or[0] + prix
        print ("Vous avez maintenant",or_,"d'or.")
        _or[0] = or_ 
        print ("Vous avez maintenant",exptotale,"d'experience.")
        exp[0] = exptotale
        niveaux()




#Attaque du personnage
def attaquer(nom,attaqueMonstre,vieMonstre,niveauMonstre):
    degats = 0
    lavie = vie[0]
    print("Que faîtes vous ? : ")
    sleep(0.25)
    print("Si vous attaquez, vous ne pourrez pas sortir du combat avant votre mort ou celle de l'ennemis.")
    sleep(0.5)
    print("Vous attaquez(1)")
    sleep(0.25)
    print("Vous fuyez(2)")
    sleep(0.25)
    choix = input ("Votre choix : ")
    if (choix == "1"):
        while (lavie>0) and (vieMonstre>0):
            print("Vous attaquez !")
            sleep(1)
            echec = randint(1,20)
            if echec >1:
                at = attaque[0]
                niv = niveau[0]
                att = randint(at-niv,at+niv)
                if att == (at+niv):
                    print ("Coup critique !")
                    sleep(0.25)
                print("Vous infligez",att,"dégats !")
                vieMonstre = vieMonstre-att
                if vieMonstre<=0:
                    recompense(nom,niveauMonstre)
                    lavie= vie[0]
                else:
                    if nom == "orc":
                        print("L'"+nom, "n'a plus que",vieMonstre,"points de vie !")
                    else :
                        print("Le",nom, "n'a plus que",vieMonstre,"points de vie !")
                sleep(0.5)
            else:
                print("Vous avez echoué à attaquer. Dommage")
                sleep(0.5)
            if vieMonstre>0:
                echec2 = randint(1,15)
                if echec2 >1:
                    print("Il attaque !")
                    sleep(1)
                    attMonstre1 = int(attaqueMonstre-0.5*niveauMonstre)
                    attMonstre2 = int(attaqueMonstre+0.5*niveauMonstre)
                    attMonstre = randint(attMonstre1,attMonstre2)
                    if attMonstre == attMonstre2 and vieMonstre >0 :
                        print("Vous subissez des dégats critiques !")
                        sleep(0.25)
                    degats = attMonstre
                    print("Vous perdez",degats,"points de vie.")
                    lavie = lavie-degats
                    vie[0] = lavie
                    sleep(2)
                    if lavie<=0:
                        print("Game Over")
                        sleep(0.25)
                        print("Vous vous êtes fait tué !")
                        sleep(0.25)
                        print("Vous ferez mieux la prochaine fois !")
                        sleep(2)
                        exit()
                    print("Il vous reste",lavie,"points de vie.")
                    sleep(1)
                else :
                    if nom == "orc":
                        print("L'"+nom,"a échoué à vous attaquer ! Vous êtes chanceux.")
                    else:
                        print("Le",nom,"a échoué à vous attaquer ! Vous êtes chanceux.")
                    sleep(0.5)
        vie[0] = lavie
    else :
        print("Vous quittez le combat !\n")
        vie[0] = lavie
        statut(classe)



#Commande pour chaser
def chasser():
    r = randint(1,3)
    if r == 1:
        nom = "loup"
        niveauMonstre = randint(niveau[0]-1,niveau[0]+1)
        vieMonstre = 5+2*niveauMonstre
        attaqueMonstre = 2+niveauMonstre
        print("Vous rencontrez un loup niveau",niveauMonstre,"!")
        sleep(0.25)
        attaquer(nom,attaqueMonstre,vieMonstre,niveauMonstre)
    if r == 2:
        nom = "goblin"
        niveauMonstre = randint(niveau[0]-1,niveau[0]+1)
        vieMonstre = 5+1.25*niveauMonstre
        attaqueMonstre = 3+0.5*niveauMonstre
        print("Vous rencontrez un goblin niveau",niveauMonstre,"!")
        sleep(0.25)
        attaquer(nom,attaqueMonstre,vieMonstre,niveauMonstre)
    if r == 3:
        nom = "orc"
        niveauMonstre = randint(niveau[0]-1,niveau[0]+1)
        vieMonstre = 7+2.5*niveauMonstre
        if niveauMonstre == 1:
            attaqueMonstre = 1.5
        else:
            attaqueMonstre = niveauMonstre+1
        print("Vous rencontrez un orc niveau",niveauMonstre,"!")
        sleep(0.25)
        attaquer(nom,attaqueMonstre,vieMonstre,niveauMonstre)

#A mettre après chaque input pour voir la commande utilisée
def commandes(classe):
    global vietotale
    global avancee
    global presenceville
    entree = input("Que faîtes vous ? : ")
    print()
    entree = entree.upper()
    if (avancee >= 1) and (presenceville == 0) and (entree == "VILLE") or (entree == "0"):
        print("Vous retournez en ville.")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        presenceville = 1
        ville1()
    elif (entree == "INVENTAIRE") or ( entree == "1"):
        print ( "Inventaire :")
        sleep(0.25)
        for i in range (len(inventaire)):
            print("-"+inventaire[i])
        sleep(0.5)
        print()



#Affiche la liste des commandes
def listeCommandes():
    global avancee
    global presenceville
    if (avancee >= 1) and (presenceville == 0) :
        print ("-Ville(0)")
        sleep(0.5)
    print("-Inventaire(1)")
    sleep(0.5)
    print("-Chasser(2)")
    sleep(0.5)
    print("-Utiliser une potion(3)")
    sleep(0.5)
    print("-Classe(4)")
    sleep(0.5)
    print("-Help(5)")
    sleep(0.5)
    if (avancee >= 1) and (presenceville == 1) :
        print("-Shop(6)")
        sleep(0.5)
        print("-Hotel(7)")
        sleep(0.5)
        print("-Partir(8)")
        sleep(0.5)
    if (avancee >= 1) and (presenceville == 0) :
        print ("-La mort(10)")
        sleep(0.5)


#Ville
def ville1():
    global classe
    global avancee
    global presenceville
    if (avancee == 1):
        print("Vous arrivez à la ville.")
        sleep(0.5)
        print(listeCommandes())
        sleep(0.5)
        commandes(classe)
        presenceville = 0
    elif (avancee == 0):
        print("Soudain,")
        sleep(0.5)
        print("Vous voyez une maison au loin , vous décidez donc de vous approcher.")
        sleep(2)
        print("En vous approchant, vous découvrez une nouvelle ville, Limoges !!!")
        sleep(2)
        print("Un habitant semble vous parler : \n ")
        sleep(2)
        print("-Bonjour et bienvenue à Limoges! \n")
        sleep(2)
        print("-Euuuh , bonjour je suis un peu perdu et je cherche un foyer pour cette nuit. \n")
        sleep(2)
        print("-Aucun soucis, alors voici notre hotel nommé 'L'ibis budget' où vous pourriez passer vos nuits ! \n")
        sleep(2)
        print("-Sympas. \n")
        sleep(2)
        print("-Ensuite, voilà notre magasin de vêtements apellé 'ZARA'! \n")
        sleep(2)
        print("-Cela m'est égal, je suis un",classe,"je cherche a vaincre des monstres afin d'affronter le Roi Démon! \n")
        sleep(2)
        print("-Alors j'ai ce qu'il faut pour vous, Voici notre tout nouveau magasin de potion pour se soigner! \n")
        sleep(2)
        print("-Parfait, c'est ce dont j'ai besoin! \n")
        sleep(2)
        print("-Pour finir voici la fôret des démons où se trouvent des loups, des orcs et des gobelins et bien evidemment le Roi Démon. \n")
        sleep(2)
        print("-Interressant! \n")
        sleep(2)
        print("-C'est tout monsieur le", classe,"! \n")
        sleep(2)
        print("-Merci bien et bonne journée! \n")
        sleep(2)
        print("-Bonne journée cher",classe,"! \n")
        sleep(2)
        avancee += 1
        print("Vous pouvez maintenant acceder au shop !")
        sleep(0.5)
        print("Faîtes 'Shop' ou '6' pour y acceder quand vous êtes en ville. \n")
        sleep(1)
        print("Vous pouvez maintenant acceder a l'hotel !")
        sleep(0.5)
        print("Faîtes 'Hotel' ou '7' pour y acceder quand vous êtes en ville.\n")
        sleep(1)
        presenceville = 0


#A mettre après chaque input pour voir la commande utilisée
def commandes(classe):
    global vietotale
    global avancee
    global presenceville
    entree = input("Que faîtes vous ? : ")
    print()
    entree = entree.upper()
    if (avancee >= 1) and (presenceville == 0) and (entree == "VILLE") or (entree == "0"):
        print("Vous retournez en ville.")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        presenceville = 1
        ville1()
    elif (entree == "INVENTAIRE") or ( entree == "1"):
        print ( "Inventaire :")
        sleep(0.25)
        for i in range (len(inventaire)):
            print("-"+inventaire[i])
        sleep(0.5)
        print()

    elif (entree == "CHASSER") or ( entree == "2"):
        presenceville = 0
        chasser()
        print()
    elif ( entree == "UTILISER") or ( entree == "3"):
        utiliser()
        print()
    elif ( entree == "CLASSE") or ( entree == "4"):
        statut(classe)
        print()
    elif ( entree == "HELP") or ( entree == "5"):
        print ( "Liste des commandes :")
        listeCommandes()
        print()
    elif  (avancee >= 1) and (presenceville == 1) :
        if ( entree == "SHOP") or (entree == "6"):
            shop()
        elif ( entree == "HOTEL") or (entree == "7"):
            hotel()
        elif ( entree == "PARTIR") or (entree == "8"):
            print("Vous quittez la ville.")
            presenceville = 0
    elif (avancee >= 1) and (presenceville == 0) :
        if (entree == "LA MORT") or (entree == "10"):
            lamort()
    if (entree !=""):
        commandes(classe)


#Combat final
def lamort():
    print("Vous vous baladiez tranquilement en éxécutant vos ennemis tandis que tout à coup, le Roi démon apparait !")
    sleep
    nom = "Roi Démon"
    niveauMonstre = 10
    vieMonstre = 100
    attaqueMonstre = 50
    print("C'est donc toi, Héros choisit par le grand mage, qui veut m'affronter ?")
    sleep(0.5)
    print("Soit, viens et meurt !")
    sleep(0.5)
    attaquer(nom,attaqueMonstre,vieMonstre,niveauMonstre)


#Nous donne nos infos de classe
def statut (classe):
    print("Classe :",classe)
    sleep(0.25)
    niv = niveau[0]
    print("Niveau :",niv)
    sleep(0.25)
    lavie = vie[0]
    print("Vie :",lavie,"/",vietotale)
    sleep(0.25)
    att = attaque[0]
    print("Attaque :",att)
    sleep(0.25)
    po = _or[0]
    print("Or :",po)
    exptotale = exp[0]
    print("Expérience :",exptotale)

#Hotel
def hotel():    
    print("Vous allez a l'hotel.")
    sleep(0.5)
    print("Vous vous dirigez donc vers l'hôtel pour passer une bonne nuit")
    sleep(0.5)
    print("-Bonjour monsieur, souhaitez vous reserver une chambre?")
    sleep(0.5)
    print("-Oui s'il vous plait.")
    sleep(0.5)
    print("-Pas de soucis, notre chambre classique coûte 3 pièces d'or (4 pv) mais nous avons la chambre de luxe qui vous fera redevenir aussi fort que vous étiez de base mais le prix est de 15 pièces d'or (max pv).")
    sleep(0.5)
    print("Vous disposez de", _or[0] ," pièces d'or.")
    sleep(0.5)
    print("Que choisissez vous, la chambre classique(1) ou notre chambre de luxe(2)?")
    sleep(0.5)
    print("Vous pouvez aussi partir(3).")
    sleep(0.5)
    k = input("C'est à vous: ")
    sleep(0.5)
    if (k == "1"):
        if _or[0] >3:
            print ("Je suis désolé mais vous n'avez pas assez d'argent.")
            sleep(0.5)
        else:
            print("je vais vous prendre la chambre classique !")
            sleep(0.5)
            _or[0]-=3
            vie[0] += 4
            print("Zzz")
            sleep(2)
            print("Vous vous êtes bien reposé.")
            sleep(0.5)
            print(statut(classe))
    elif (k == "2"):
        if _or[0] >15:
            print ("Je suis désolé mais vous n'avez pas assez d'argent.")
        else:
            _or[0] -= 15
            vie[0] = vietotale
            print("Zzzzzzzz....")
            sleep(2)
            print("C'était vraiment votre meilleure nuit de sommeil depuis un long moment.")
            sleep(0.5)
            print(statut(classe))
    elif ( k == "3"):
        print("C'est trop cher pour vous, vous partez d'ici.")
        sleep(0.5)
    faire()




#Stats de base
niveau = [1]
classe = "Paysan"
attaque = [2+2*niveau[0]]
vietotale = 10+3*niveau[0]
vie = [vietotale]
inventaire=["Potion","Potion"]
_or = [5]
exp = [0]
avancee = 0
presenceville = 0

#Introduction
print ("Vous vous réveillez un beau matin, et une voix venue de nulle part semble vous parler.")
sleep(0.5)
print ("Bonjour et bienvenue, noble paysan, moi, le grand mage Paysouf t'ai choisi afin que tu libères le monde du règne du maléfique Roi Démon.")
sleep(0.5)
print ("Je vais te donner les bases.\n")
sleep(0.5)
print("Attention, répondez avec des chiffres au cours de votre aventure lorsque vous voyez (1) ou (2) ou (...).")
sleep(0.5)

print ("Tu pourras toujours utiliser la commande 'help' pour demander la liste des commandes.")
sleep(0.5)
print ( "La voici :\n")
listeCommandes()
print()
sleep(0.5)
print("Tapez la touche entrer pour skiper.\n")
sleep(0.5)

#Test des premières commandes
faire()

t = input("Tu a compris ? ")
"\n"
t=t.upper()
if (t == "NON"):
    print("Dommage.")
    print()
else : print("Très bien.\n")




#Choix de la classse
print ("Tu vas maintenant choisir ta classe !")
sleep(0.5)
def choixdeclasse():
    global classe
    global vietotale
    global avancee
    choix = input("Choisi entre Épéiste(1) et Magicien(2) : ")
    sleep(0.5)
    choix = choix.upper()
    if (choix == "1") or (choix == "EPEISTE") or (choix == "ÉPEISTE") or (choix == "EPÉISTE") or (choix == "EPEISTE(1)") or (choix == "ÉPEISTE(1)") or (choix == "EPÉISTE(1)"):
        classe =  "Épéiste"
        attaque[0] = 2+2*niveau[0]
        vietotale = 10+4*niveau[0]
        print("Tu es maintenant un Épéiste !")
    elif (choix == "2") or (choix == "MAGICIEN") or (choix == "MAGICIEN(2)"):
        classe = "Magicien"
        attaque[0] = 2+4*niveau[0]
        vietotale = 10+3*niveau[0]
        print("Tu es maintenant un Magicien !")
    elif (choix == ""):
        print()
        choixdeclasse()
    
    elif choix == "456789":
        classe = "Dieu créateur"
        attaque[0] = 1000000
        vietotale = 1000000
        vie[0] = 1000000
        avancee = 10000000
        exp[0]
        print("Bienvenue, Dieu créateur.")

    
    else :
        print ( "Ce n'était pas parmis les choix, tu restera un paysan !")
        sleep(0.5)
        classe = "Paysan"
        attaque[0] = 2+2*niveau[0]
        vietotale = 10+3*niveau[0]
        print("Tu as essayé de me brain, tu sera la classe la plus nulle.")
    sleep(0.75)
    
choixdeclasse()
faire()

#L'histoire commmence
print ("Vous vous situez dans une petite maison perdu dans les bois.")
sleep(1)
print ("Voulez vous aller chercher de la vie ou explorer la foret.\n")
sleep(1)

def aventure1():
    print("Choisi entre Aller vers le nord chercher de la vie(1), Aller à l'aventure courageusement en foret(2) et Rester chez soi par flemmardise(3). \n ")
    n = input("C'est à vous :")
    if (n == "2"):
        print ("Tandis que vous vous promenez en foret , vos sens de",classe,"vous font remarquer une présence derrière vous.")
        sleep(2)
        print ("En vous retournant, vous apercevez un ours au loin vous foncer droit dessus!")
        sleep(2)
        print ("COUREZ !!!")
        sleep(1)
        print ("Malheureusement, vous êtes un",classe,"et n'êtes donc pas assez rapide!")
        sleep(2)
        print ("Vous succombez sous les morsures de l'ours.")
        sleep(2)
        exit()

    elif (n == "3"):
        print("Vous avez autre choses à faire que ces conneries et retournez à vos occupations.")
        sleep(2)
        exit()

    elif (n == "1"):
        print("Vous allez donc vers le nord pour chercher de la vie comme on vous l'a appris dans 'Man VS Wild' \n")
        sleep(1)
        ville1()

    else :
        print("Choisissez une commande valable!")
        aventure1()

aventure1()
    

print("Vous pensez: Pourquoi pas ne pas perdre de temps et aller explorer la fôret dont il m'a parler et combattre un peu?")
sleep(0.5)
print("Choisissez entre passer une bonne nuit pour être en meilleur forme le lendemain mais vous devrez payer l'hotel(Vous disposez de", _or[0] ," pièces d'or.)(1) ou aller explorer la fôret(2) \n ")
sleep(0.5)
n = input("C'est à vous: ")
sleep(0.5)
if (n == "1"):
    hotel()
elif ( n=="2") :
    print("Vous allez donc chasser des monstres pour vous defouler !")
    sleep(0.5)
    chasser()
faire()


sleep(3)