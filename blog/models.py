from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
    
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100, null=True)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add= True, auto_now = False, verbose_name = "Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete = models.DO_NOTHING, null=True )

    def __str__(self):
        return self.titre
    
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.EmailField()
    photo = models.ImageField(upload_to="photos/")
   
    def __str__(self):
        return self.nom
        

