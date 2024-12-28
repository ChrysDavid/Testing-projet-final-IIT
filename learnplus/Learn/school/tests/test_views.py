import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@pytest.mark.django_db
def test_login_view_authenticated_instructor(client):
    user = User.objects.create_user(username="instructor", password="password")
    client.login(username="instructor", password="password")
    response = client.get(reverse("login"))
    assert response.status_code == 302  # Redirection vers le tableau de bord

@pytest.mark.django_db
def test_login_view_guest(client):
    response = client.get(reverse("login"))
    assert response.status_code == 200
    assert "pages/guest-login.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_signup_view(client):
    response = client.get(reverse("guests_signup"))
    assert response.status_code == 200
    assert "pages/guest-signup.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_forgot_password_view(client):
    response = client.get(reverse("forgot_password"))
    assert response.status_code == 200
    assert "pages/guest-forgot-password.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_islogin_success(client):
    user = User.objects.create_user(username="student", password="password")
    response = client.post(
        reverse("post"),
        content_type="application/json",
        data={"username": "student", "password": "password"},
    )
    assert response.status_code == 200
    assert response.json()["success"] is True

@pytest.mark.django_db
def test_islogin_failure(client):
    response = client.post(
        reverse("post"),
        content_type="application/json",
        data={"username": "wronguser", "password": "wrongpassword"},
    )
    assert response.status_code == 200
    assert response.json()["success"] is False

@pytest.mark.django_db
def test_deconnexion_view(client):
    user = User.objects.create_user(username="instructor", password="password")
    client.login(username="instructor", password="password")
    response = client.get(reverse("deconnexion"))
    assert response.status_code == 302
    assert response.url == reverse("login")
