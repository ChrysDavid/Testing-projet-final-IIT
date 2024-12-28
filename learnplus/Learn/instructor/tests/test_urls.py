import pytest
from django.urls import reverse, resolve
from instructor import views

@pytest.mark.parametrize("url_name,view_func,args", [
    ('dashboard', views.dashboard, None),
    ('instructor-account-edit', views.account_edit, None),
    ('course-edit', views.course_edit, {'slug': 'test-slug'}),
    ('course-add', views.course_add, None),
    ('instructor-courses', views.courses, None),
    ('instructor-matiere', views.matiere, {'slug': 'test-slug'}),
    ('instructor-forum', views.forum, None),
    ('instructor-forum-ask', views.forum_ask, None),
    ('instructor-forum-thread', views.forum_thread, {'slug': 'test-slug'}),
    ('instructor-lesson-add', views.lesson_add, {'slug': 'test-slug'}),
    ('instructor-lesson-edit', views.lesson_edit, {'id': '1', 'slug': 'test-slug'}),
    ('instructor-messages', views.messages, {'classe': 'test-class'}),
    ('instructor-profile', views.profile, None),
    ('instructor-quiz-edit', views.quiz_edit, {'quiz_id': 1}),
    ('instructor-quiz-add', views.quiz_add, None),
    ('instructor-review-quiz', views.review_quiz, None),
    ('instructor-quizzes', views.quizzes, None),
    ('instructor-add_question', views.add_question, {'quiz_id': 1}),
    ('post_cours', views.post_cours, None),
    ('delete_chapitre', views.delete_chapitre, None),
    ('delete_lesson', views.delete_lesson, None),
    ('post_lesson', views.post_lesson, None),
    # ('update_profil', views.update_profil, None),
    # ('update_password', views.update_password, None),
    ('instructor_post_forum', views.post_forum, None),
])

def test_url_resolves(url_name, view_func, args):
    if args:
        path = reverse(url_name, kwargs=args)
    else:
        path = reverse(url_name)
    assert resolve(path).func == view_func
