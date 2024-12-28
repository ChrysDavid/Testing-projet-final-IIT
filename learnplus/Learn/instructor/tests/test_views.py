import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from instructor.models import Instructor
from school.models import Chapitre, Cours, Matiere, Classe, Niveau

@pytest.mark.django_db
def test_dashboard_view_as_instructor(client):
    user = User.objects.create_user(username="instructor", password="password")
    niveau = Niveau.objects.create(nom="Niveau Test")  # Créez un niveau si nécessaire
    classe = Classe.objects.create(numeroClasse=5, niveau=niveau)
    instructor = Instructor.objects.create(user=user, classe=classe)
    Matiere.objects.create(nom="Mathématiques", status=True, instructors=[instructor])
    client.login(username="instructor", password="password")

    response = client.get(reverse("dashboard"))
    assert response.status_code == 200
    assert "pages/instructor-dashboard.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_account_edit_view_as_instructor(client):
    user = User.objects.create_user(username="instructor", password="password")
    Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-account-edit"))
    assert response.status_code == 302
    assert "pages/instructor-account-edit.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_course_add_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(titre="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    Matiere.objects.create(nom="Physique", status=True, instructors=[instructor])
    client.login(username="instructor", password="password")

    response = client.get(reverse("course-add"))
    assert response.status_code == 200
    assert "pages/instructor-course-add.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_course_edit_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(titre="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    chapitre = Chapitre.objects.create(titre="Chapitre Test", classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("course-edit", kwargs={"slug": chapitre.slug}))
    assert response.status_code == 200
    assert "pages/instructor-course-edit.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_courses_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(titre="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    Chapitre.objects.create(titre="Chapitre Test", classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-courses"))
    assert response.status_code == 200
    assert "pages/instructor-courses.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_matiere_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(titre="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    matiere = Matiere.objects.create(nom="Physique", status=True, instructors=[instructor])
    Chapitre.objects.create(titre="Chapitre Test", matiere=matiere, classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-matiere", kwargs={"slug": matiere.slug}))
    assert response.status_code == 200
    assert "pages/instructor-cours-chap.html" in [t.name for t in response.templates]

from forum.models import Sujet

@pytest.mark.django_db
def test_forum_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(titre="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    Sujet.objects.create(titre="Sujet général", question="Question ?", cours=None)
    Sujet.objects.create(titre="Sujet classe", question="Question ?", cours__chapitre__classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-forum"))
    assert response.status_code == 200
    assert "pages/instructor-forum.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_forum_ask_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-forum-ask"))
    assert response.status_code == 200
    assert "pages/instructor-forum-ask.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_forum_thread_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    forum = Sujet.objects.create(titre="Sujet Test", question="Question ?", cours=None)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-forum-thread", kwargs={"slug": forum.slug}))
    assert response.status_code == 200
    assert "pages/instructor-forum-thread.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_lesson_add_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    chapitre = Chapitre.objects.create(titre="Chapitre Test", slug="chapitre-test", classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-lesson-add", kwargs={"slug": chapitre.slug}))
    assert response.status_code == 200
    assert "pages/instructor-lesson-add.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_lesson_edit_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    chapitre = Chapitre.objects.create(titre="Chapitre Test", slug="chapitre-test", classe=classe)
    cours = Cours.objects.create(titre="Cours Test", slug="cours-test", chapitre=chapitre)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-lesson-edit", kwargs={"slug": cours.slug, "id": chapitre.id}))
    assert response.status_code == 200
    assert "pages/instructor-lesson-edit.html" in [t.name for t in response.templates]


from chat.models import Salon

@pytest.mark.django_db
def test_messages_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    salon = Salon.objects.create(classe=classe)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-messages", kwargs={"classe": classe.id}))
    assert response.status_code == 200
    assert "pages/instructor-messages.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-profile"))
    assert response.status_code == 200
    assert "pages/instructor-profile.html" in [t.name for t in response.templates]


from quiz.models import Quiz

@pytest.mark.django_db
def test_quiz_edit_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    quiz = Quiz.objects.create(titre="Quiz Test", id=1, instructor=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-quiz-edit", kwargs={"quiz_id": quiz.id}))
    assert response.status_code == 200
    assert "pages/instructor-quiz-edit.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_quiz_add_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-quiz-add"))
    assert response.status_code == 200
    assert "pages/instructor-quiz-add.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_quiz_add_post_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.post(
        reverse("instructor-quiz-add"),
        {
            "titre": "New Quiz",
            "time_value": 2,
            "time_unit": "hour",
        }
    )
    assert response.status_code == 302  # Redirection après ajout
    assert Quiz.objects.filter(titre="New Quiz").exists()


@pytest.mark.django_db
def test_quizzes_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    Quiz.objects.create(titre="Quiz Test", instructor=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-quizzes"))
    assert response.status_code == 200
    assert "pages/instructor-quizzes.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_review_quiz_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-review-quiz"))
    assert response.status_code == 200
    assert "pages/instructor-review-quiz.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_statement_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.get(reverse("instructor-statement"))
    assert response.status_code == 200
    assert "pages/instructor-statement.html" in [t.name for t in response.templates]



@pytest.mark.django_db
def test_post_cours(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    matiere = Matiere.objects.create(nom="Mathématiques")
    client.login(username="instructor", password="password")

    response = client.post(
        reverse("post_cours"),
        {
            "title": "Chapitre 1",
            "matiere": matiere.id,
            "duration": 10,
            "description": "Description du chapitre",
        }
    )
    assert response.status_code == 200
    assert Chapitre.objects.filter(titre="Chapitre 1").exists()

@pytest.mark.django_db
def test_delete_chapitre(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    chapitre = Chapitre.objects.create(titre="Chapitre Test", classe=classe)
    client.login(username="instructor", password="password")

    response = client.post(reverse("delete_chapitre"), {"id": chapitre.id})
    assert response.status_code == 200
    assert not Chapitre.objects.filter(id=chapitre.id).exists()

@pytest.mark.django_db
def test_post_lesson(client):
    user = User.objects.create_user(username="instructor", password="password")
    classe = Classe.objects.create(nom="Classe Test")
    instructor = Instructor.objects.create(user=user, classe=classe)
    chapitre = Chapitre.objects.create(titre="Chapitre Test", classe=classe)
    client.login(username="instructor", password="password")

    response = client.post(
        reverse("post_lesson"),
        {
            "title": "Lesson 1",
            "chapitre": chapitre.id,
            "description": "Description de la leçon",
        }
    )
    assert response.status_code == 200
    assert Chapitre.objects.filter(titre="Lesson 1").exists()



from forum.models import Sujet

@pytest.mark.django_db
def test_update_profil(client):
    user = User.objects.create_user(username="instructor", password="password")
    instructor = Instructor.objects.create(user=user)
    client.login(username="instructor", password="password")

    response = client.post(
        reverse("update_profil"),
        {
            "nom": "New Last Name",
            "prenom": "New First Name",
            "email": "newemail@test.com",
            "bio": "New bio",
        }
    )
    user.refresh_from_db()
    assert response.status_code == 200
    assert user.last_name == "New Last Name"
    assert user.first_name == "New First Name"
    assert user.email == "newemail@test.com"
    assert instructor.bio == "New bio"

@pytest.mark.django_db
def test_update_password(client):
    user = User.objects.create_user(username="instructor", password="oldpassword")
    client.login(username="instructor", password="oldpassword")

    response = client.post(
        reverse("update_password"),
        {
            "last_password": "oldpassword",
            "new_password": "newpassword",
            "confirm_password": "newpassword",
        }
    )
    assert response.status_code == 200
    user.refresh_from_db()
    assert user.check_password("newpassword")

@pytest.mark.django_db
def test_post_forum(client):
    user = User.objects.create_user(username="instructor", password="password")
    client.login(username="instructor", password="password")

    response = client.post(
        reverse("post_forum"),
        {
            "titre": "Nouveau Sujet",
            "question": "Contenu de la question",
        }
    )
    assert response.status_code == 200
    assert Sujet.objects.filter(titre="Nouveau Sujet").exists()