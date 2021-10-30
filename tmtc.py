import requests
import isbnlib
from isbnlib.registry import bibformatters
from isbnlib import meta

try :
    with open('fichierSource.csv', 'r+')as file:
        for ligne in file:
            cleaned = ligne.rstrip()

            #LIBRARY
            print("OpenLibrary")
            url = "https://openlibrary.org/api/books?bibkeys=ISBN:"+cleaned+"&callback=mycallback"
            payload = {}
            header = {}
            response = requests.request("GET", url, header = headers, data = payload)
            print(response.text)
            #GoogleBooks
            print("Google Books")
            query = 'isbn:'+cleaned
            params = {"q": query}
            url = 'https://www.googleapis.com/books/v1/volumes'
            response = requests.get(url, params=params)
            print(response.text)

            print("AltMetrics")
            url = "https://api.altmetric.com/v1/isbn/"+cleaned
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)


except FileNotFoundError:
    print("Fichier introuvable")
except IOError:
    print("erreur d’ouverture")