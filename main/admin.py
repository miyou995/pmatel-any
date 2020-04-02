from django.contrib import admin

# Register your models here.
from .models import Valeur, Solution, Partenaires, Actualite, Marque, Produit, Categorie, Secteur
# Register your models here.

class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'client_ou_fournisseur', 'logo')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'marque','categorie', 'recommander')
    prepopulated_fields = {"slug": ("nom",)}
    list_display_links = ('id','nom')
    list_per_page = 40
    list_editable = ['recommander']
    list_filter = ('marque', 'categorie', 'recommander')
    search_fields = ('id', 'nom', 'marque', 'categorie', )
    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'marque')
    list_filter = ('marque', 'secteur',)
    search_fields = ('id', 'nom')
    prepopulated_fields = {"slug": ("nom",)}

class SecteurAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nom')
    prepopulated_fields = {"slug": ("nom",)}

class MarqueAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nom')
    prepopulated_fields = {"slug": ("nom",)}
class SolutionAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nom')
    prepopulated_fields = {"slug": ("nom",)}

admin.site.register(Marque, MarqueAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Secteur, SecteurAdmin)
admin.site.register(Valeur)
admin.site.register(Actualite)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Partenaires, PartenaireAdmin)