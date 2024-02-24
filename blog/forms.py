from django import forms
from .models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse E-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie", required = False)

    #il peut arriver qu'on veuille controler encore plus les données entrée pour un champ
    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
        
        return message
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'auteur', 'slug', 'contenu','categorie')

class NouveauForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.EmailField()
    photo = forms.ImageField()