#python test_cmd3.py get book "Dr. Kaitlyn Ratke"
#python test_cmd3.py get books 10
#python test_cmd3.py get commentaires 0180338d-9d81-4057-bed4-b876012e8ead
#
import argparse
import sys
import requests
import urllib.parse

acts = ['get', 'post', 'patch']
quoi = ['book', 'books', 'auteur', 'commentaires', 'review']
p = argparse.ArgumentParser()
if sys.argv[1:]:
    p.add_argument('action', choices = acts)
    p.add_argument('quoi', choices = quoi)
    p.add_argument(dest='qui', action="store")
    #p.add_argument('qui', action="store")
    #parser.add_argument("-a", "--auteur", action="store", help="autor name")
    #p.add_argument('action', nargs = '*', choices = acts)
else:
    p.add_argument('--action', default = 'get')

args = p.parse_args()
#print(args)
""" print(args.action)
print(args.quoi)
print(args.qui) """

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

def books(n):
    url = 'https://demo.api-platform.com/books?order[publicationDate]=desc&page=1'
    r_books = requests.get(url)
    dico_books = r_books.json()
    liste_books = dico_books.get("hydra:member")
    liste_books = liste_books[0:n]
    for i in range(len(liste_books)):
        for k, v in liste_books[i].items():
            if k == 'title':
                t = v
            if k == 'publicationDate':
                d = v
                d = d[0:10]
                print(d, ' : ', t)
    #print(liste_books)

def commentaires(id):
    livre = "https://demo.api-platform.com/books/"+ id
    livre = requests.get(livre)
    #print(livre)
    dico_livre = livre.json()
    liste_comments = dico_livre.get('reviews')
    for i in range(len(liste_comments)):
        for k, v in liste_comments[i].items():
            if k == 'body':
                print(v)


if args.action == 'get':
    if args.quoi == 'book':
        livres(args.qui)
    elif args.quoi == 'books':
        n = int(args.qui)
        books(n)
    elif args.quoi == 'commentaires':
        commentaires(args.qui)