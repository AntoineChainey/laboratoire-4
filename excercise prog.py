a=1
while a == 1 :                  #boucle vérifie si l'age de l'utilisateur est valide
    age = input("quelle est votre age en chiffre: ")    #demande age utilisateur age = age utilisateur
    try :                       #essaye si la fonction marche
        age = float(age)            #change type pour float age
        a = 0
    except ValueError :         #sinon renvoie a la boucle
        print("ce n'est pas un nombre valide")   
test1 = 0               #test1 = clé sortie de la boucle
while test1 == 0 :      #boucle pour recommencer quand la réponse est incorrect
    if age < 18 :         #classe l'utilisateur dans sa catégorie d'age.
        print("vous avez",age,"ans")    #confirme l'age de l'utilisateur
        consommation = input("buver vous de l'alcool: ")        #définis si l'utilisateur consomme
        if consommation == "oui" :                             
            test2 = 0
            while test2 == 0 :
                print("chaque jour, chaque semaine, chaque mois, autre")
                rythmeconsommation = input("a quel fréquence consommer vous: ")     #définis a quel fréquence l'utilisateur consomme
                if rythmeconsommation == "chaque jour":                             #boucle sur les autre groupe d'age
                    print("merci pour votre réponse")                               # ajouter un fichier qui regroupe les réponse
                    test2 = 1 
                    test1 = 1
                elif rythmeconsommation == "chaque semaine":
                    print("merci pour votre réponse")
                    test2 = 1 
                    test1 =1
                elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                    print("bravo merci pour votre réponse")
                    test2 = 1
                    test1 = 1
                else:
                    print("réponse incorect")           #affiche qu'il y a eu un probleme dans la réponse renvoie a la question au dessus
                    test1 = 1
        elif consommation == "non":         
            print("bravo")
            test1 = 1 
        else:
            print("réponse incorrect")                  
    elif age >= 18 and age < 30 :                   
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                break
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                break
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                break
            else:
                print("réponse incorect")        
        elif consommation == "non":
            print("bravo") 
            break
        else:
            print("réponse incorrect")
    elif age >= 30 and age < 50 :
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect")          
        elif consommation == "non":
            print("bravo")
            test1 = 1 
        else:
            print("réponse incorrect")
    elif age >= 50 :
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect") 
        elif consommation == "non":
            print("bravo") 
            test1 = 1
        else:
            print("réponse incorrect")
    else :
        print("réponse incorect")
personne = [age, consommation, rythmeconsommation ]  #repertorie les information recueillis plius haut

with open("mon_fichier.txt", "a") as fichier:
    fichier.write(f"Age: {age}, Consommation: {consommation}, Rythme: {rythmeconsommation}\n") # ouvre u n fichier texte et y inscris les information selon leur classe

print("les informations ont été reccueilis.")

b = True                                        #définis la variable
while b == True :       #boucle du deuxieme questionnaire
    continuer = input("voulez vous continuer: ")            #demande si l'utilisateur veut passer au deuxieme questionnaire
    if continuer == "oui" :                     #condition pour savoir si l'utilisateur continue
        consommation_drogue = input("consommer vous de la drogue: ")  # demande si l'utilisateur consomme de la drogue
        if consommation_drogue == "oui" :
            a=5
            for i in range(a) :                 # boucle qui permet de répété la question si la réponse est invallide
                fréquence_drogue = input("consommez-vous chaque semaine: ") #demande si l'utilisateur consomme chaque semaine a condition que la réponse précédente sois oui
                if fréquence_drogue == "oui" :
                    print("vous consommez chaque semaine")
                    break                   # renvoie a la fin du quiz
                elif fréquence_drogue == "non" :
                    print("vous ne consommez pas chaque semaine")
                    continue        #recommence la boucle.
                else :
                    print("réponse incorrect")
                    continue
            b = False
            c = 5    
            for i in range(c) :  #la boucle ce répete pour toutes les valeurs comprise dans le range c
                fréquence_drogue = input("consommez vous chaque mois: ")    
                if fréquence_drogue == "oui" :
                    print("vous consommez chaque mois")
                    break
                elif fréquence_drogue == "non" :
                    print("vous ne consommez pas chaque mois")
                    d = 5    
                    for i in range(d) :   
                        fréquence_drogue = input("vous consommez a une autre fréquence que celle proposer: ")
                        if fréquence_drogue == "oui" :
                            fréquence_drogue = input("a quel fréquence consommer vous: ")
                            break
                        elif fréquence_drogue == "non" :
                            print("vous avez répondue non le questionnaire recommence.")
                            continue
                        else :
                            print("réponse invallide")
                            continue
            b = False
                else :
                    print("réponse incorrect")
                    continue
            b = False
            d = 5    
            for i in range(d) :   
                fréquence_drogue = input("vous consommez a une autre fréquence que celle proposer: ")
                if fréquence_drogue == "oui" :
                    fréquence_drogue = input("a quel fréquence consommer vous: ")
                    break
                    
                elif fréquence_drogue == "non" :
                    print("vous avez répondue non le questionnaire recommence.")
                    continue
                else :
                    print("réponse invallide")
                    continue
            b = False
        elif consommation_drogue == "non" :
            print("vous ne consommez pas de drogue")
            b = False
        else :
            print("réponse incorrect")
    elif continuer == "non" :
        print("le test est finis")
        b = False
    else :
        print("réponse incorrect")
        continue


        


