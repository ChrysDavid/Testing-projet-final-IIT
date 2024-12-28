import pytest
from django.contrib.auth.models import User
from forum.models import Sujet, Reponse
from school.models import Cours

@pytest.mark.django_db
def test_create_sujet():
    user = User.objects.create_user(username="testuser", password="password")
    cours = Cours.objects.create(titre="Cours Test", description="Description Test")
    sujet = Sujet.objects.create(
        user=user,
        cours=cours,
        question="Quelle est la meilleure méthode pour apprendre Django ?",
        titre="Apprendre Django"
    )
    assert sujet.user == user
    assert sujet.cours == cours
    assert sujet.question == "Quelle est la meilleure méthode pour apprendre Django ?"
    assert sujet.titre == "Apprendre Django"
    assert sujet.slug.startswith("apprendre-django")

@pytest.mark.django_db
def test_create_reponse():
    user = User.objects.create_user(username="testuser", password="password")
    cours = Cours.objects.create(titre="Cours Test", description="Description Test")
    sujet = Sujet.objects.create(
        user=user,
        cours=cours,
        question="Quelle est la meilleure méthode pour apprendre Django ?",
        titre="Apprendre Django"
    )
    reponse = Reponse.objects.create(
        user=user,
        sujet=sujet,
        reponse="En suivant la documentation officielle."
    )
    assert reponse.user == user
    assert reponse.sujet == sujet
    assert reponse.reponse == "En suivant la documentation officielle."
    assert reponse.slug.startswith("apprendre-django")
