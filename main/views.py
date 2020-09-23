from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

app_name = "main"

Mensaje = "holaaaaaaa"

import pprint 
import requests 


secret = "5f039f3f100a42cdbc4aa9661082475f"

# Define the endpoint 
url = 'http://newsapi.org/v2/everything?'

# Specify the query and 
# number of returns 
parameters = { 
	'q': 'rebrote', # query phrase 
    'pageSize': 100, # maximum is 100 
 	'apiKey': secret, # your own API key 
    'language': 'es',

} 

# Make the request 
response = requests.get(url, 
						params = parameters) 

# Convert the response to 
# JSON format and pretty print it 
response_json = response.json()

class articulo:
    def __init__(self, article):
        self.titulo = article['title']
        self.descripcion = article['description']
        self.url = article['url']
        self.urlImagen = article['urlToImage']
        self.fecha = article['publishedAt']
        self.autor = article['author']
        self.nombre = article['source']['name']

def extraerArticulosAPI(response_json):
    for a in response_json['articles']:
        yield(articulo(a))

articulos = list(extraerArticulosAPI(response_json))

import feedparser    

feedsPolitica = [
        { 'diario': 'Gestión', 'urlfeed': "http://espresso.gestion.pe/feed/politica"},
        { 'diario': 'El Comercio', 'urlfeed': "https://archivo.elcomercio.pe/feed/politica.xml" },
        { 'diario': 'La República', 'urlfeed': "https://larepublica.pe/rss/politica.xml?outputType=rss" },
        { 'diario': 'Peru.com', 'urlfeed': "https://peru.com/feed/actualidad/politicas" },
        ]


def extraerArticulos(feeds):
    for feed in feeds:
        rss = feedparser.parse(feed['urlfeed'])
        for item in rss['entries']:
            article = dict()
            article['title'] = item['title']
            article['description']= item['summary']
            article['url'] = item['link']
            article['urlToImage'] = '#'
            article['publishedAt'] = item['published']
            article['author'] = ''
            article['source']= dict() 
            article['source']['name']= feed['diario']
            yield articulo(article)
            
articulos = list(extraerArticulos(feedsPolitica))


def homepage(request):
    return render(request, "main/inicio.html", {"news":articulos,}) #recibe dato, nomplantilla y diccionario de variables(opcional)
    #return HttpResponse("Hola mundo") #por ahora retorna una http