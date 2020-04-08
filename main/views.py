from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Valeur, Solution , Partenaires, Marque, Secteur, Produit, Categorie

from main.forms import ContactForm
from . import forms
from django.core.mail import send_mail, EmailMessage

# Create your views here.
class Index(ListView):
    model = Valeur
    template_name = 'index.html'
    context_object_name = 'valeurs'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        context['secteurs'] = Secteur.objects.all()
        return context
        

class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        return context



class SolutionsView(ListView):
    model = Solution
    template_name = 'solutions.html'
    context_object_name = 'solutions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        return context


class SolutionDetailView(DetailView):
    model = Solution
    template_name = 'solution_detail.html'
    context_object_name = 'solution'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        return context    

class PartenairesView(ListView):
    model = Partenaires
    template_name = 'partenaires.html'
    context_object_name = 'partenaires'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Partenaires.objects.filter(client_ou_fournisseur__exact='CL')
        context['fournisseurs'] = Partenaires.objects.filter(client_ou_fournisseur__exact='FR')
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        return context


class Hotel(TemplateView):
    template_name= 'hotel.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        return context    


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/"


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
    
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            if form.cleaned_data.get('file'):
                file = request.FILES['file']

            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)

            try:
                mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['hello@octopus-consulting.com']) 
                if form.cleaned_data.get('file'):
                    mail.attach(file.name, file.read(), file.content_type)
                mail.send()
                # print('email envoyer')
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})
                # print('l"email nest pas envoyer')
        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
        

def error404(request, exception):
    return render(request, '404.html', status=404)



# la class MarqueDetail est la vue qui affiche la page d'une marque avec les produits de la marque, une seul marque, une liste de produits

class MarqueDetail(ListView):
    model = Produit
    template_name='marque.html'
    context_object_name = 'produits_marque'

    def get_queryset(self):
        self.marque = get_object_or_404(Marque, slug=self.kwargs['slug'])
        return Produit.objects.filter(marque=self.marque)
    
    def get_context_data(self, **kwargs):
        context = super(MarqueDetail, self).get_context_data(**kwargs)
        context['marque'] = self.marque
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        context['marquesExtars'] = Marque.objects.exclude(produit__isnull=True)
        return context
    
# la class ProduitDetail est la vue qui affiche la page d'un seul produit avec la fiche technique et tt
class ProduitDetail(DetailView):
    model = Produit
    template_name = 'detail_produit.html'
    context_object_name = 'produit'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        context['marquesExtars'] = Marque.objects.exclude(produit__isnull=True)
        context['categorie']= Categorie.objects.all()
        return context
#cla class CategorieList est la pages de tous les produits et categorie normalement elle devrais afficher les secteur ainsi que tous les produits  
# chaque secteur avec ses categories 
# chaque ctegorie renvoie vers une page de Categorie Details 
class ProduitsList(ListView):
    paginate_by = 25
    model = Produit
    context_object_name = 'produits'
    template_name='produits.html'
    
    def get_queryset(self):
        
        query = self.request.GET.get('q')
        if query != None:
            produits = Produit.objects.filter(
               Q(nom__icontains = query) | Q(categorie__nom__icontains = query)
                )
        else:
            produits = Produit.objects.all()
        return produits

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        context['marquesExtars'] = Marque.objects.exclude(produit__isnull=True)
        context['secteurs'] = Secteur.objects.all()

        return context

# c'est la page d'une seul categorie qui affiche tous les produits d'une seul categorie
class CategorieDetail(ListView):
    model = Produit
    template_name= 'detail_categorie.html'
    context_object_name = 'produits'

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, slug=self.kwargs['slug'])
        return self.categorie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produits'] = Produit.objects.filter(categorie=self.categorie)
        context['categorie'] = self.categorie
        context['solutions'] = Solution.objects.all()
        context['marques'] = Marque.objects.exclude(produit__isnull=True)
        context['marquesExtars'] = Marque.objects.exclude(produit__isnull=True)
        context['recommander'] = Produit.objects.filter(recommander = True)

        return context

#c'est une vue de detail de secteurs        Categories par secteurs
class CategorieList(ListView):
    model = Categorie
    template_name = 'categorie.html'
    context_object_name = 'categories'

    def get_queryset(self):
        self.secteur = get_object_or_404(Secteur, slug= self.kwargs['slug'])
        return self.secteur
    
    def get_context_data(self, **kwargs):
        context = super(CategorieList, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.filter(secteur= self.secteur)
        context['secteur'] = self.secteur
        context['solutions'] = Solution.objects.all()
        context['produits'] = Produit.objects.all()
        return context


class Catalogue(TemplateView):
    template_name= 'catalogue.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solutions'] = Solution.objects.all()
        context['categories'] = Categorie.objects.all()
        context['habitat'] = Categorie.objects.filter(secteur__id__exact = 1 )
        context['industrie'] = Categorie.objects.filter(secteur__id__exact = 2 )
        context['installations'] = Categorie.objects.filter(secteur__id__exact = 3 )
        context['marques'] = Marque.objects.exclude(produit__isnull=True)

        return context    





