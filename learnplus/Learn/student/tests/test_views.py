import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student
from quiz.models import Quiz, Devoir, QuizResult
from school.models import Classe, Chapitre, Cours, Niveau, Matiere
from forum.models import Sujet

@pytest.mark.django_db
def test_index_view_authenticated(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("index_student"))
    assert response.status_code == 302
    assert "pages/fixed-student-dashboard.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_payment_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("billing"))
    assert response.status_code == 302
    assert "pages/fixed-student-account-billing-payment-information.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_subscription_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("subscription"))
    assert response.status_code == 302
    assert "pages/fixed-student-account-billing-subscription.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_edit_profile_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("edit-profile"))
    assert response.status_code == 302
    assert "pages/fixed-student-account-edit-profile.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_cart_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("cart"))
    assert response.status_code == 302
    assert "pages/fixed-student-cart.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_my_courses_view(client):
    user = User.objects.create_user(username="student", password="password")
    niveau = Niveau.objects.create(nom="Licence 1")
    classe = Classe.objects.create(niveau=niveau, numeroClasse=101)
    Student.objects.create(user=user, classe=classe)
    client.login(username="student", password="password")
    response = client.get(reverse("my-courses"))
    assert response.status_code == 302
    assert "pages/fixed-student-my-courses.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_quiz_list_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    Quiz.objects.create(titre="Quiz 1", temps=30)
    client.login(username="student", password="password")
    response = client.get(reverse("quiz-list"))
    assert response.status_code == 302
    assert "pages/fixed-student-quiz-list.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_take_quiz_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    quiz = Quiz.objects.create(titre="Quiz 1", temps=30)
    client.login(username="student", password="password")
    response = client.get(reverse("take-quiz", kwargs={"quiz_id": quiz.id}))
    assert response.status_code == 302
    assert "pages/fixed-student-take-quiz.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_submit_quiz(client):
    user = User.objects.create_user(username="student", password="password")
    quiz = Quiz.objects.create(titre="Quiz 1", temps=30)
    client.login(username="student", password="password")
    response = client.post(
        reverse("submit-quiz", kwargs={"quiz_slug": quiz.slug}),
        content_type="application/json",
        data={"answers": {}, "timeTaken": 300}
    )
    assert response.status_code == 200
    assert response.json()["success"] is False

@pytest.mark.django_db
def test_post_forum(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    matiere = Matiere.objects.create(nom="Mathématiques")
    chapitre = Chapitre.objects.create(titre="Chapitre Test", matiere=matiere)
    cours = Cours.objects.create(titre="Cours 1", chapitre=chapitre)
    client.login(username="student", password="password")
    response = client.post(
        reverse("post_forum"),
        {"titre": "Sujet 1", "question": "Test", "lesson": cours.id}
    )
    assert response.status_code == 200
    assert Sujet.objects.filter(titre="Sujet 1").exists()

@pytest.mark.django_db
def test_view_course_view(client):
    user = User.objects.create_user(username="student", password="password")
    Student.objects.create(user=user)
    client.login(username="student", password="password")
    response = client.get(reverse("view-course"))
    assert response.status_code == 302
    assert "pages/fixed-student-view-course.html" in [t.name for t in response.templates]
