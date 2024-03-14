from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db import connection
from django.db.models import Q
from miapp.forms import FormArticulo
from django.contrib import messages

# Create your views here.
layout = ""

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

#tarea
def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre ="Ana", apellidos = "Perez")
    return render(request,'pagina.html' , {'texto':'Este es mi texto', 'lista':['uno','dos','tres'],})

#actividad 29 de febrero
def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
def articulo (request):
    try:
        articulo = Article.objects.get(pk=7, public= False)
        response = f"Articulo consultado: {articulo.title} - {articulo.content} - Estado: {articulo.public}"
    except:
        response = "<strong>Articulo no encontrado<strong>"

    return HttpResponse(response)
def editar_articulo(request):
    articulo = Article.objects.get(pk=7)
    articulo.title = "los 12 cuentos peregrinos"
    articulo.public = True
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre {articulo.title} ha sido actualizado y su estado es: {articulo.public}")

def articulos(request):
    articulos = Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos':articulos
    })

#actividad 06 de marzo
def borrarArticulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def deleteArticulo(request, id):

    Temp = (f"DELETE FROM miapp_Article WHERE id = %s")
    with connection.cursor () as cursor:
        cursor.execute(Temp, [id])

        articulos = Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos':articulos
    })

def updateArticulo (request, title, id):
    Temp = (f"UPDATE miapp_article SET title = %s WHERE id = %s")
    with connection.cursor() as cursor:
        cursor.execute(Temp, [title,id])
        articulos= Article.objects.all()
    return render(request, 'articulos.html', {
        'articulos':articulos
    })


#clase 8 de marzo
def saveArticulo(request):
    if  request.method == 'POST':
        title = request.POST ["title"]
        if len (title)<=5:
            return HttpResponse("El titulo del articulo debe ser mayor a 5 caracteres")
        else:
            content = request.POST['content']
            public = request.POST['public']

    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def createArticulo(request):
    return render(request, 'createArticulo.html')

#
def create_full_articulo(request):
    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get ('public')

            articulo= Article(
                title = title,
                content= content,
                public = public,
            )
            articulos = Article.objects.all().order_by('content')

            articulo.save()
            #crea un mensaje flash (sesion que solo se muestra una vez)
            messages.success(request, f'El articulo {articulo.id} se ha guardado satisfactoriamente')
            #return HttpResponse (title + ' '+ content + ' ' + str(articulo.public))
            return render(request,'articulos.html',{
                'titulo':'Guardado el articulo con exito',
                'icono': 'sucess',
                'boton': 'aceptar',
                'articulos' : articulos
            })
        else:
            
            return render (request,'create_full_articulos.html',{
                'form':formulario})
    else:
        formulario = FormArticulo()
        return render (request,'create_full_articulos.html',{
            'form':formulario
        })






# def articulos(request):
#     articulos = Article.objects.order_by('id')
#     articulos = Article.objects.filter(title = "articulo 4")
#     articulos = Article.objects.filter(public = "True",id=4)
#     articulos = Article.objects.filter(title__contains="articulos")
#     articulos = Article.objects.filter(title__exact="articulos")
#     articulos = Article.objects.filter(title__iexact="rticulos")
#     articulos = Article.objects.filter(title__iexact="articulos 4")
    articulos = Article.objects.filter(id__gt=1)
    articulos = Article.objects.filter(id__lte=5)
    articulos = Article.objects.filter(id__in=[1,2,9,10])
    articulos = Article.objects.filter(
                                title__contains="L",
                                public=True 
                                
                                    ).exclude(
                                        
                                    )
    articulos = Article.objects.order_by('id')
    articulos = Article.objects.filter(
                Q(title_contains="") | Q (public = True)
)