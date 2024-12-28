import pytest
from quiz.models import Quiz, Devoir, Question, Reponse, QuizResult, QuestionResponse
from django.contrib.auth.models import User
from school.models import Chapitre

@pytest.mark.django_db
def test_create_quiz():
    user = User.objects.create_user(username="instructor", password="password")
    quiz = Quiz.objects.create(
        instructor=user,
        titre="Quiz Test",
        temps=30
    )
    assert quiz.instructor == user
    assert quiz.titre == "Quiz Test"
    assert quiz.temps == 30
    assert quiz.slug is not None

@pytest.mark.django_db
def test_create_devoir():
    chapitre = Chapitre.objects.create(titre="Chapitre Test")
    devoir = Devoir.objects.create(
        sujet="Sujet Test",
        dateDebut="2024-01-01T08:00:00Z",
        dateFermeture="2024-01-10T17:00:00Z",
        chapitre=chapitre,
        coefficient=2,
        support="path/to/file.pdf"
    )
    assert devoir.sujet == "Sujet Test"
    assert devoir.chapitre == chapitre
    assert devoir.coefficient == 2
    assert devoir.slug is not None

@pytest.mark.django_db
def test_create_question():
    quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
    question = Question.objects.create(
        quiz=quiz,
        title="Quelle est la capitale de la France ?",
        question_type="qcm",
        score=10,
        timeframe_enabled=True,
        timeframe_duration=5,
        timeframe_unit="minute"
    )
    assert question.quiz == quiz
    assert question.title == "Quelle est la capitale de la France ?"
    assert question.question_type == "qcm"
    assert question.score == 10

@pytest.mark.django_db
def test_create_reponse():
    quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
    question = Question.objects.create(quiz=quiz, title="Capitale de l'Allemagne ?", question_type="qcm", score=5)
    reponse = Reponse.objects.create(
        question=question,
        reponse="Berlin",
        is_True=True
    )
    assert reponse.question == question
    assert reponse.reponse == "Berlin"
    assert reponse.is_True is True

@pytest.mark.django_db
def test_create_quiz_result():
    user = User.objects.create_user(username="student", password="password")
    quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
    result = QuizResult.objects.create(
        student=user,
        quiz=quiz,
        score=85.0,
        total_questions=10,
        correct_answers=8,
        completion_time=600
    )
    assert result.student == user
    assert result.quiz == quiz
    assert result.score == 85.0
    assert result.total_questions == 10
    assert result.correct_answers == 8

@pytest.mark.django_db
def test_create_question_response():
    user = User.objects.create_user(username="student", password="password")
    quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
    question = Question.objects.create(quiz=quiz, title="Capitale du Japon ?", question_type="qcm", score=5)
    result = QuizResult.objects.create(student=user, quiz=quiz, score=80.0, total_questions=10, correct_answers=8, completion_time=600)
    response = QuestionResponse.objects.create(
        quiz_result=result,
        question=question,
        selected_answer="Tokyo",
        is_correct=True
    )
    assert response.quiz_result == result
    assert response.question == question
    assert response.selected_answer == "Tokyo"
    assert response.is_correct is True
