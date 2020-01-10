#Q2 Afficher les livres écrits par l’auteur « Dr. Kaitlyn Ratke »
# ligne de commande à passer
#python livres_auteur.py "Dr. Kaitlyn Ratke"
# résultat attendu
# 1997-07-04  :  Similique aut est dolores.

import argparse
import requests
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("auteur", type=str, help="saisir le nom de l'auteur")
args = parser.parse_args()
auteur = args.auteur
auteur = urllib.parse.quote(auteur)

def livres(auteur):
    url = "https://demo.api-platform.com/books/?author=" + auteur
    r_auteur = requests.get(url)
    dico_auteur = r_auteur.json()
    lst_books_auteur = dico_auteur.get("hydra:member")
    for i in range(len(lst_books_auteur)):
        for k, v in lst_books_auteur[i].items():
            if k == 'title':
                t = v
            if k == 'publicationDate':
                d = v
                d = d[0:10]
        print(d, ' : ', t)

livres(auteur)