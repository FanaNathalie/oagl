# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:54:11 2022

@author: fana
"""
from select import select
import sqlite3

#ouvrir une connexion ou créer un fichier si une base de données n'existe pas
connexion = sqlite3.connect("tp5_exo.db")

#création du curser sur les différentes table
curseur_produits = connexion.cursor()
curseur_clients = connexion.cursor()
curseur_fourmisseur = connexion.cursor()
curseur_categorie = connexion.cursor()

#Exécution unique
# création des base des tables 

curseur_produits.execute('''CREATE TABLE IF NOT EXISTS produits
                    ( id_produit TEXT PRIMARY KEY, 
                    nom_pro TEXT, 
                    prix_un, 
                    categorie_pro TEXT)
                    ''')

curseur_clients.execute('''CREATE TABLE IF NOT EXISTS clients
                    ( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    nom_client,
                    cmd_cl TEXT,
                    qt_pro INTEGER)
                    ''')

curseur_fourmisseur.execute('''CREATE TABLE IF NOT EXISTS fourmisseur
                    (nom_fss,      
                    nom_pro TEXT,
                    cat_pro TEXT,
                    qt_pro INTEGER)
                ''')
curseur_categorie.execute('''CREATE TABLE IF NOT EXISTS categorie
                    ( nom_cat TEXT PRIMARY KEY,
                    qt_pro INTEGER)
                ''')             


#Exécution d'un script 
# enrégistre plusieurs produits
curseur_produits.executescript('''
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("T23G", "Tomate", "100", "fruie");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("RI90", "Riz", "25000", "aliments");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("AS23", "Anana", "500", "fruie");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("B23C", "Parle_G", "100", "Biscuit");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("BM23", "Cho_co", "200", "Biscuit");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("CO23", "You_pi", "250", "Biscuit");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("O234", "Orange", "50", "fruie");
                      INSERT INTO produits(id_produit, nom_pro, prix_un, categorie_pro) VALUES ("L345", "Lemon", "100", "fruie")
                      ''')
# enrégistrement de la clients de plusieurs clients
curseur_clients.executescript('''
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("fana olinga", "Tomate", "10");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("Alima", "Tomate", "25");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("fana olinga", "Riz", "2");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("Junior", "Parle_G", "20");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("Junior", "Cho_co", "15");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("Yoyo", "You_pi", "25");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES (" fana olinga", "Orange", "56");
                      INSERT INTO clients(nom_client, cmd_cl, qt_pro) VALUES ("fana olinga", "Cho_co", "10")
                      ''')

# enrégistrment d'un fournisseur
curseur_fourmisseur.execute('''
                    INSERT INTO fourmisseur(nom_fss, nom_pro, cat_pro, qt_pro) VALUES ("nathalie", "Riz", "aliment", "20")
                            ''')
            
curseur_categorie.execute('''
                      INSERT INTO categorie(nom_cat, qt_pro) VALUES ("aliment", "20")
                      ''')

connexion.commit()


#sections dans notre base de donées

# afficher la liste des proguits
print("------la liste des produits --------------------")
curseur_produits.execute("SELECT COUNT(*) FROM produits")
print("le nombre total des produits :",curseur_produits.fetchone())
for produit in curseur_produits.execute("SELECT id_produit, nom_pro FROM produits"):
    print("prduit :", produit)

# afficher la liste des clients
print("------la liste des clients --------------------")
# curseur_clients.execute("SELECT COUNT(*) FROM clients")
# print("le nombre des clients: ",curseur_clients.fetchone())

x= 0
for client in curseur_clients.execute("SELECT nom_client FROM clients GROUP BY nom_client"):
    print("client :", client)
    x = x + 1
print("le nombre des clients: ", x)

#la liste des produits d'un client donné
print("------la des produits d'un client donné --------------------")
cli_pro = ("fana olinga",)
# curseur_clients.execute("SELECT cmd_cl FROM clients WHERE nom_client = ?", cli_pro)
# print(curseur_clients.fetchone())
print("les produits du client: ", cli_pro)
for client_pro in curseur_clients.execute("SELECT cmd_cl FROM clients WHERE nom_client = ? GROUP BY cmd_cl", cli_pro):
    print("produit_client :", client_pro)

# la facture d'un client donné
print("------la facture d'un client donné --------------------")
cli_fac = ("fana olinga",)
# curseur_clients.execute("SELECT cmd_cl, prix_un, qt_pro, (prix_un * qt_pro) FROM clients INNER JOIN produits ON cmd_cl = nom_pro WHERE nom_client = ?", cli_fac)
# print(curseur_clients.fetchone())

print("les produits du client: ", cli_pro)
for client_fac in curseur_clients.execute("SELECT cmd_cl, prix_un, qt_pro, (prix_un * qt_pro) FROM clients INNER JOIN produits ON cmd_cl = nom_pro WHERE nom_client = ? GROUP BY cmd_cl", cli_fac):
    print("facture d'un produit :", client_fac)

# curseur_clients.execute("SELECT (prix_un * qt_pro) Somme FROM clients INNER JOIN produits ON cmd_cl = nom_pro WHERE nom_client = ? GROUP BY cmd_cl", cli_fac)
# print("Votre Facture total est de: ",curseur_clients.fetchone())

fac = 0
for client_fac in curseur_clients.execute("SELECT (prix_un * qt_pro) FROM clients INNER JOIN produits ON cmd_cl = nom_pro WHERE nom_client = ? GROUP BY cmd_cl", cli_fac):
    fac = fac + int(client_fac[0])
print("-------Facture--------")
print("Votre facture est :", fac)


connexion.close()     
