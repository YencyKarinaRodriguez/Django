from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def hola_mundo (request):
    return render (request,'hola_mundo.html')

def saludo (request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre = "Ana", apellido = "Andrade")
    return render (request,'saludo.html')

def presentacion (request):
    return render (request,'presentacion.html')

def index (request):
    template = """
                    <h1>Inicio</h1>
                    <p>Años desde el 2024 hasta 2050</p>
                     <ul>
                 """
    year=2024
    while year <= 2050:
        template += f"<li> {str(year)} </li>"
        year += 1
    template += """</ul><hr>"""

    
    template += """
                    <h1>Años biciestos</h1>
                    <ul>
                """
    year1 = 2024
    while year1 <= 2050:
        if year1 % 4 == 0:
            template += f"<li>{str(year1)}</li>"
        year1 += 1
    template += """</ul><hr>"""

    template += """
                <h1>Años pares</h1>
                <ul>
                """
    year2 = 2024
    while year2 <= 2050:
        if year2 % 2 == 0:
            template += f"<li>{str(year2)}</li>"
        year2 += 1
    template += """</ul><hr>"""
    nombre = ''

    return render (request,'index.html', {
    'mi_variable': 'soy un dato que esta en la vista',
    'title': 'inicio del sitio',
    'titulo': 'Pagina inicio SENA',
    'name': nombre
    })

def contacto (request, nombre = "", apellido = ""):
    aprendiz = ""
    if nombre and apellido:
        aprendiz += f"<h3>{nombre} {apellido}</h3>"
    elif nombre:
        aprendiz += f"<h2>Nombre: {nombre}</h2>"
    elif apellido:
        aprendiz += f"<h2>Apellido: {apellido}</h2>"
    else:
        aprendiz += f"<h2>Nombre y Apellido inexistente</h2>"
        
    #return HttpResponse(layout + f"<h2>Contacto: </h2>" + aprendiz)
    return render (request,'contacto.html')

def quienesSomos (request):

    return render (request, 'quienesSomos.html')

def productoServicios (request):

    return render (request, 'productoServicio.html')

#t
def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre ="Ana", apellidos = "Perez")
    return render(request,'pagina.html' , {'texto':'Este es mi texto', 'lista':['uno','dos','tres'],})