from django.shortcuts import render
from . import marvel

def index(request):
    return render(request, 'core/index.html')

def personagens(request):
    cabecalho_string = marvel.cabecalho()
    url_sufix = 'characters'
    marvel_json = marvel.get_marvel_json(url_sufix, cabecalho_string)
    print(marvel_json)
    if request.POST:
        if 'pesquisaunica': 
            print('pesquisaunica')
        elif 'pesquisalista':
            print('pesquisalista')
    return render(request, 'core/personagens.html')