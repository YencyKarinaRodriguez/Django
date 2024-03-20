from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="artticles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    create_date = models.DateTimeField(auto_now_add = True, verbose_name="Fecha Creacion")
    update_date = models.DateField(auto_now = True, verbose_name="Fecha Actualizacion")

    class Meta:
        #dab_table=""
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id'] #o tambien ['-id'] para ejecutar descente
    def __str__(self):
        if self.public:
            publico = "(Publicado)"
        else:
            publico = "(Privado)"
        return f"{self.title} -> {publico}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    create_date = models.DateField()
