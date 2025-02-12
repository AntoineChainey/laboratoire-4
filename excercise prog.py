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
