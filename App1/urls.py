from django.urls import path
from App1.views import LogInView, SignUpView

urlpatterns=[
    path('/signup',SignUpView.as_view()),
    path('/login', LogInView.as_view()),
]

