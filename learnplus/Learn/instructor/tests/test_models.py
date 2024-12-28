import pytest
from django.contrib.auth.models import User
from instructor.models import Instructor
from school.models import Classe, Matiere
from quiz.models import Question

@pytest.mark.django_db
def test_create_instructor():
    """Test de création d'un instructeur avec tous les champs requis."""
    user = User.objects.create_user(username="testinstructor", password="password")
    classe = Classe.objects.create(name="Classe Test")
    instructor = Instructor.objects.create(
        user=user,
        contact="123456789",
        adresse="123 Rue Exemple",
        classe=classe,
        bio="Bio de test"
    )
    assert instructor.user == user
    assert instructor.contact == "123456789"
    assert instructor.classe == classe
    assert instructor.bio == "Bio de test"
    assert instructor.slug == "testinstructor"

@pytest.mark.django_db
def test_instructor_many_to_many_matieres():
    """Test de l'ajout de matières à un instructeur via la relation ManyToMany."""
    user = User.objects.create_user(username="testinstructor", password="password")
    classe = Classe.objects.create(name="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    
    matiere1 = Matiere.objects.create(nom="Mathématiques")
    matiere2 = Matiere.objects.create(nom="Physique")
    instructor.matieres.add(matiere1, matiere2)
    
    assert instructor.matieres.count() == 2
    assert matiere1 in instructor.matieres.all()
    assert matiere2 in instructor.matieres.all()

@pytest.mark.django_db
def test_instructor_many_to_many_questions():
    """Test de l'ajout de questions à un instructeur via la relation ManyToMany."""
    user = User.objects.create_user(username="testinstructor", password="password")
    classe = Classe.objects.create(name="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    
    question1 = Question.objects.create(title="Question 1", score=5)
    question2 = Question.objects.create(title="Question 2", score=10)
    instructor.questions.add(question1, question2)
    
    assert instructor.questions.count() == 2
    assert question1 in instructor.questions.all()
    assert question2 in instructor.questions.all()

@pytest.mark.django_db
def test_instructor_save_method():
    """Test de la méthode `save` pour la génération automatique du slug."""
    user = User.objects.create_user(username="testinstructor", password="password")
    classe = Classe.objects.create(name="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    
    assert instructor.slug == "testinstructor"

@pytest.mark.django_db
def test_instructor_get_u_type():
    """Test de la propriété `get_u_type`."""
    user = User.objects.create_user(username="testinstructor", password="password")
    instructor = Instructor.objects.create(user=user)
    
    assert instructor.get_u_type is True

@pytest.mark.django_db
def test_instructor_string_representation():
    """Test de la représentation sous forme de chaîne de caractères."""
    user = User.objects.create_user(username="testinstructor", password="password")
    instructor = Instructor.objects.create(user=user)
    
    assert str(instructor) == "testinstructor"
