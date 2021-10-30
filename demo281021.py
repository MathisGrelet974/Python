
import requests
import isbnlib
from isbnlib.registry import bibformatters
from isbnlib import meta
#from isbnlib import ISBNLibException
#from isbnlib.dev._exceptions import NoDataForSelectorError
#rint(isbnlib.cover(isbn))

try:
    with open('fichierSource.csv', 'r+') as file:
        for ligne in file:
            cleaned = ligne.rstrip()
            #Open Library
            print("OpenLibrary")
            url = "https://openlibrary.org/api/books?bibkeys=ISBN:%22+cleaned+%22&callback=mycallback"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)

            #GoogleBooks
            print("Google Books")
            query = 'isbn:'+cleaned
            params = {"q": query}
            url = 'https://www.googleapis.com/books/v1/volumes'
            response = requests.get(url, params=params)
            print(response.text)
            #data = json.load(response.json())
            #print(response.json()['items'][0]['volumeInfo']['title'])
            #print(data)

            #AltMetrics
            print("AltMetrics")
            url = "https://api.altmetric.com/v1/isbn/%22+cleaned"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)

except FileNotFoundError:
    print("Fichier introuvable")
except IOError:
    print("erreur d’ouverture")