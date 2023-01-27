import requests
import bs4

#url para iterar
link_base = "http://books.toscrape.com/catalogue/page-{}.html"

#seleccion de titulos con raigting alto

titulos_seleccionados = []

# iteracion de paginas
for numero_de_pagina in range(1,51):
    # Soup en cada pagina de interes
    url_busqueda = link_base.format(numero_de_pagina)
    busqueda = requests.get(url_busqueda)
    soup= bs4.BeautifulSoup(busqueda.text, 'lxml')

    #seleccion de libros
    libros = soup.select('.product_pod')
    
    #iterar libros
    for libro in libros:
        #chequeo de raiting
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #guardar titulo en nuestra variable:

            titulos_chequeados = libro.select('a')[1]['title']

            titulos_seleccionados.append(titulos_chequeados)
# ver nuestra seleccion de libros
for titulo in titulos_seleccionados:
    print(titulo)


