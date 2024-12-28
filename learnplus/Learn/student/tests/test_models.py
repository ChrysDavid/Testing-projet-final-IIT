import pytest
from student.models import Student, StudentReponse
from django.contrib.auth.models import User
from school.models import Classe

@pytest.mark.django_db
def test_create_student():
    user = User.objects.create_user(username="student", password="password")
    classe = Classe.objects.create(niveau="Licence 1", numeroClasse=101)
    student = Student.objects.create(user=user, classe=classe, bio="Bio de test")
    assert student.user == user
    assert student.classe == classe
    assert student.bio == "Bio de test"
    assert student.slug is not None

@pytest.mark.django_db
def test_student_get_u_type():
    user = User.objects.create_user(username="student", password="password")
    student = Student.objects.create(user=user)
    assert student.get_u_type is True

@pytest.mark.django_db
def test_create_student_reponse():
    student = Student.objects.create(user=User.objects.create_user(username="student"))
    reponse = StudentReponse.objects.create(
        student=student, question="Quelle est la capitale de la France ?", reponse="Paris"
    )
    assert reponse.student == student
    assert reponse.question == "Quelle est la capitale de la France ?"
    assert reponse.reponse == "Paris"
