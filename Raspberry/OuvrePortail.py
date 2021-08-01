import telnetlib
import time
import sys


try:
    tn = telnetlib.Telnet("10.100.0.1", 8035)
except :
    print("Echec Connexion")
    exit(1)


if (int(sys.argv[1]) == 1) :
    #Demande Ouverture du Portail
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "dra_ejm_utl36:DRA_EJM_entrée portail");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()


if (int(sys.argv[1]) == 2) :
    #Demande Ouverture du Portillon
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "ejm-utl39:EJM portillon Pk");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()


if (int(sys.argv[1]) == 3) :
    #Demande Ouverture de la Borne de recharge
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "ejm-utl38:EJM-borne ZE");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()

if (int(sys.argv[1]) == 4) :
    #Demande Ouverture du portail accès cuisine
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "ejm-utl38:EJM portail cours");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()

if (int(sys.argv[1]) == 5) :
    #Demande Ouverture de la porte coté école primaire
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "ejm-utl36:DRA_EJM_entrée principale");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()

if (int(sys.argv[1]) == 6) :
    #Demande Ouverture du local informatique
    try:
        tn.write('login(api-rmi,Davidapi);setRmiCommandConnection(true);execute(provideAccess, "ejm-utl39:EJM local info");\n'.encode('utf-8'))
    except :
        print("Erreur envoi commande")
        pass
    time.sleep(5)
    tn.close()