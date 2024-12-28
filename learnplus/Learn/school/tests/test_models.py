import pytest
from school.models import Filiere, Matiere, Niveau, Classe, Chapitre, Cours
from django.contrib.auth.models import User
from instructor.models import Instructor

@pytest.mark.django_db
def test_create_filiere():
    filiere = Filiere.objects.create(nom="Informatique")
    assert filiere.nom == "Informatique"
    assert filiere.status is True

@pytest.mark.django_db
def test_create_matiere():
    matiere = Matiere.objects.create(nom="Mathématiques")
    assert matiere.nom == "Mathématiques"
    assert matiere.status is True
    assert matiere.slug is not None

@pytest.mark.django_db
def test_create_niveau():
    niveau = Niveau.objects.create(nom="Licence 1")
    assert niveau.nom == "Licence 1"
    assert niveau.status is True
    assert niveau.slug is not None

@pytest.mark.django_db
def test_create_classe():
    niveau = Niveau.objects.create(nom="Licence 1")
    filiere = Filiere.objects.create(nom="Informatique")
    classe = Classe.objects.create(niveau=niveau, numeroClasse=101, filiere=filiere)
    assert classe.niveau == niveau
    assert classe.numeroClasse == 101
    assert classe.filiere == filiere

@pytest.mark.django_db
def test_create_chapitre():
    niveau = Niveau.objects.create(nom="Licence 1")
    filiere = Filiere.objects.create(nom="Informatique")
    classe = Classe.objects.create(niveau=niveau, numeroClasse=101, filiere=filiere)
    matiere = Matiere.objects.create(nom="Algèbre")
    chapitre = Chapitre.objects.create(
        titre="Chapitre 1",
        classe=classe,
        matiere=matiere,
        duree_en_heure=10,
        description="Introduction à l'algèbre"
    )
    assert chapitre.titre == "Chapitre 1"
    assert chapitre.classe == classe
    assert chapitre.matiere == matiere

@pytest.mark.django_db
def test_create_cours():
    niveau = Niveau.objects.create(nom="Licence 1")
    filiere = Filiere.objects.create(nom="Informatique")
    classe = Classe.objects.create(niveau=niveau, numeroClasse=101, filiere=filiere)
    matiere = Matiere.objects.create(nom="Programmation")
    chapitre = Chapitre.objects.create(titre="Introduction", classe=classe, matiere=matiere)
    cours = Cours.objects.create(titre="Python", chapitre=chapitre, description="Cours de base en Python")
    assert cours.titre == "Python"
    assert cours.chapitre == chapitre
    assert cours.description == "Cours de base en Python"
