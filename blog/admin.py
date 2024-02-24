from django.contrib import admin
from blog.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')

    #configuration du formulaire d'édition
    fieldsets = (
        #fieldset 1
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'slug', 'auteur', 'categorie')
        }),

        #fieldset 2
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon excient',
            'fields': ('contenu',)
        }),
    )

    prepopulated_fields = {'slug': ('titre',),}
    #colonnes personnalisées
    def apercu_contenu(self, article):
        """ retourne les 40 premiers caractères du contenu de l'article.
         S'il y a plus de 40 caractères, il faut ajouter des points de suspension """
        
        text = article.contenu[:40]
        if len(article.contenu)>40:
            return '{}...'.format(text)
        else:
            return text
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
