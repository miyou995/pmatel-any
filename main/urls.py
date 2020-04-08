from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Index, SolutionsView, SolutionDetailView, PartenairesView, Hotel, About, ContactFormView, MarqueDetail, ProduitDetail, ProduitsList, CategorieDetail, CategorieList, Catalogue

urlpatterns = [
    path('', Index.as_view(), name= 'index'),
    path('about/', About.as_view(), name= 'about'),
    path('solutions/', SolutionsView.as_view(), name='solutions_list'),
    path('solutions/<slug:slug>', SolutionDetailView.as_view(), name='solution_detail'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('partenaires/', PartenairesView.as_view(), name='partenaires'),
    path('hotel/', Hotel.as_view(), name='hotel'),
    path('produits/', ProduitsList.as_view(), name='produits'),
    path('marque-<slug:slug>/', MarqueDetail.as_view(), name='marque'),
    path('produit/<slug:slug>/', ProduitDetail.as_view(), name='produit_detail'),
    path('categorie/<slug:slug>/', CategorieDetail.as_view(), name='categorie'),
    path('secteur/<slug:slug>/', CategorieList.as_view(), name='secteur'),
    path('catalogue/', Catalogue.as_view(), name='catalogue'),
    
] 
