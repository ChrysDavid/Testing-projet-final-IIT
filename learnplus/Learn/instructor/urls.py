from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('account_edit', views.account_edit, name='instructor-account-edit'), 
    path('course_edit', views.course_edit, name='course-edit'),
    path('courses', views.courses, name='instructor-courses'), 
    # path('earnings', views.earnings, name='earning'),
    path('edit_invoice', views.edit_invoice, name='instructor-edit-invoice'),
    path('forum', views.forum, name='instructor-forum'),
    path('forum_ask', views.forum_ask, name='instructor-forum-ask'),
    path('forum_thread', views.forum_thread, name='instructor-forum-thread'),
    path('invoice', views.invoice, name='instructor-invoice'),
    path('lesson-add', views.lesson_add, name='instructor-lesson-add'),
    path('messages', views.messages, name='instructor-messages'),
    path('profile', views.profile, name='instructor-profile'),
    path('quiz_edit', views.quiz_edit, name='instructor-quiz-edit'),
    path('review_quiz', views.review_quiz, name='instructor-review-quiz'),
    path('quizzes', views.quizzes, name='instructor-quizzes'),
    # path('statement', views.statement, name='instructor-statement'),    
]