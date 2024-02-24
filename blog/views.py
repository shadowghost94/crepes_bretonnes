from blog.forms import *
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import *
# Create your views here.

class FAQView(TemplateView):
    template_name = "blog/faq.html"

class ListArticles(ListView):
    model = Article
    context_object_name = "derniers_article"
    template_name = "blog/acceuil.html"
    paginate_by = 5
    queryset = Article.objects.filter(categorie__id=1)
    

def article_form(request):
    if (request.method == 'POST'):
        form = ArticleForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            slug = form.cleaned_data['slug']
            contenu = form.cleaned_data['contenu']
            date = form.cleaned_data['date']
            categorie = form.cleaned_data['categorie']

            envoie = True

    else:
        form = ArticleForm()
    return render (request, 'blog/templateLambda.html', locals())



def acceuil(request):
    #On affiche tous les articles
    articles= Article.objects.all()

    return render(request, 'blog/acceuil.html', {'dernier_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render (request, 'blog/lire.html', {'article': article})

def contact (request):
    #si il s'agit d'une requête HTTP de type POST
    if request.method == 'POST':
        #on reprend les données
        form = ContactForm(request.POST)
        #on vérifie ensuite si le formulaire est valide
        if form.is_valid():
            #traitement des données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            envoie = True
        
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    
    if request.method == 'POST':
        form = NouveauForm(request.POST, request.FILES)

        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True

    else:
        form = NouveauForm()

    return render(request, 'blog/nouveau_contact.html', locals())