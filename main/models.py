from django.db import models

# Create your models here.
class Valeur(models.Model):
    titre = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.titre

class Solution(models.Model):
    nom       = models.CharField(max_length=70)
    slug        = models.CharField(max_length=70)
    petit_text  = models.CharField(max_length=200, blank = True)
    marque      = models.CharField(max_length=70)
    logo        = models.ImageField(upload_to='media', blank = True)
    image       = models.ImageField(upload_to='media',blank = True)
    image2      = models.ImageField(upload_to='media',blank = True)
    image3      = models.ImageField(upload_to='media',blank = True)
    image4      = models.ImageField(upload_to='media',blank = True)
    image5      = models.ImageField(upload_to='media',blank = True)
    description = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.marque, self.nom)

class Partenaires(models.Model):
    TYPE_DE_PARTENARIAT = [
        ('CL','Client'),
        ('FR','Fournisseur'),
    ]
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/partenaires')
    client_ou_fournisseur = models.CharField(max_length=2,choices=TYPE_DE_PARTENARIAT)

    def __str__(self):
        return self.nom


class Actualite(models.Model):
    titre       = models.CharField(max_length=70)
    soustitre   = models.CharField(max_length=70)
    description = models.TextField()


class Marque(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='media/marques')

    def __str__(self):
        return self.nom 

class Secteur(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media/categorie')
  
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media/categorie')
    marque = models.ForeignKey('Marque', on_delete=models.CASCADE, blank= True, null=True)

    def __str__(self):
        return self.nom 

class Produit(models.Model):
    nom = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media/produits')
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    reference = models.CharField(max_length=200, blank = True)
    description = models.TextField(max_length=200, blank = True)
    disponible = models.BooleanField(default=True)
    recommander = models.BooleanField(default=False)
    caractéristique_1 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_1 = models.CharField(max_length=100, blank = True)
    caractéristique_2 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_2 = models.CharField(max_length=200, blank = True)
    caractéristique_3 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_3 = models.CharField(max_length=200, blank = True)
    caractéristique_4 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_4 = models.CharField(max_length=200, blank = True)
    caractéristique_5 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_5 = models.CharField(max_length=200, blank = True)
    caractéristique_6 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_6 = models.CharField(max_length=200, blank = True)
    caractéristique_7 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_7 = models.CharField(max_length=200, blank = True)
    caractéristique_8 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_8 = models.CharField(max_length=200, blank = True)
    caractéristique_9 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_9 = models.CharField(max_length=200, blank = True)
    caractéristique_10 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_10 = models.CharField(max_length=200, blank = True)
    caractéristique_11 = models.CharField(max_length=100, blank = True)
    détail_de_caractéristique_11 = models.CharField(max_length=200, blank = True)


    def __str__(self):
        return '%s - %s' % (self.marque, self.nom)