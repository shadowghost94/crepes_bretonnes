from django.urls import path
from . import views
from .models import *
from django.views.generic import ListView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.acceuil),
    path('acceuil/', views.acceuil),
    path('contact/', views.contact, name='contact'),
    path('article/<int:id>-<slug:slug>/', views.lire, name='lire'),
    path('templatesLambda/', views.article_form, name='templateLambda'),
    path('nouveau-contact/', views.nouveau_contact, name="nouveau-contact"),
    path('faq/', views.FAQView.as_view() ),
    path('listView/', ListView.as_view(model=Article, context_object_name="derniers_articles", template_name="blog/acceuil.html"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)